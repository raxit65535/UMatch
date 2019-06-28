from __future__ import print_function
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from kafka import KafkaProducer
from pyspark.streaming.kafka import KafkaUtils
import sys
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
import pygeohash as gh


'''
Precision of Geo Hash
#   km      
1   ± 2500
2   ± 630
3   ± 78
4   ± 20
5   ± 2.4
6   ± 0.61
7   ± 0.076
8   ± 0.019
9   ± 0.0024
10  ± 0.00060
11  ± 0.000074

'''
# Function to generate geo location hash based on longitude and lattitude. Precision is 5 decimal points
def geohash(x):

    array = x.strip("()").split(",")
    lon = array[0]
    lat = array[1]
    return gh.encode(float(lon), float(lat), 5)
    # print(x)


# function to Sink the computation statestics to Kafka
def kafkaSink(matched_stats):
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    # producer = KafkaProducer(bootstrap_servers = "10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092")
    producer.send('hash_matched_stats', matched_stats.encode('utf8'))
    producer.flush()

# Function to compute Herversine Distance for given two location points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1 = float(lon1)
    lat1 = float(lat1)
    lon2 = float(lon2)
    lat2 = float(lat2)
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


# function to format the message into semicolan seperated stacked values into a single variable
# Helper function to sink the matched records to kafka
def format_message_matched(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider, driver_id, driver_loc, water_mark_driver, distance, now_timestamp):
    str_fmt = "{};{};{};{};{};{};{};{};{}"
    message = str_fmt.format(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider,
                             driver_id, driver_loc, water_mark_driver, distance, now_timestamp)
    # print(message)
    return message


# function to format the message into semicolan seperated stacked values into a single variable
# Helper function to sink the updated driver location to kafka
def format_message_driver(driver_id, driver_loc, timestamp):
    str_fmt = "{};{};{}"
    message = str_fmt.format(driver_id, driver_loc, timestamp)
    # print(message)
    return message

# function to format the message into semicolan seperated stacked values into a single variable
# Helper function to sink the matched stats to kafka
def format_match_stats(total_ride_req, matched_riders, total_drivers, timestamp):
    str_fmt = "{};{};{};{}"
    message = str_fmt.format(total_ride_req, matched_riders,
                             total_drivers, timestamp)
    # print(message)
    return message


# Process the RDD and compute Greedy bipartite match
def process_union(rdd):

    # Empty data structures to keep track of Rider and Driver ids who are matched. Avoid duplicates
    matched_list = dict()
    matched_driver = dict()

    total_ride_req = dict()
    total_driver = dict()

    sink_match = list()
    sink_driver = list()

    unmatched_rider_list = []
    unmatched_driver_list = []
    
    # for each record in RDD
    for line in rdd:
        
        # Since RDD record is a tuple, seperating it into two values rider and driver
        rider, driver = line[1]
        
        # When doing left outer join, if the hash values doen't match, the driver's tuple will contain none. 
        # I define them as outliers. The if condition will ignore the outliers.
        if(driver is None or rider is None):
            continue
        # Seperating out all the values from tuple into single variables.    
        ride_pickup = rider[1].strip("()").split(",")
        driver_loc = driver[1].strip("()").split(",")
        ride_long = ride_pickup[0]
        ride_lat = ride_pickup[1]
        driver_long = driver_loc[0]
        driver_lat = driver_loc[1]

        
        # keeping the dictionary of Total riders
        if rider[0] not in total_ride_req:
            total_ride_req[rider[0]] = "new"

        # keeping the dictionary of total drivers
        if driver[0] not in total_driver:
            total_driver[driver[0]] = "new"

        # if the driver id and rider id is not in the matched dictionary
        if rider[0] not in matched_list and driver[0] not in matched_driver:
            # print("not yet matched")

            # then compute the distance between
            distance = haversine(ride_long, ride_lat, driver_long, driver_lat)
            if distance < 3:
                # print("herversine true, adding the value")
                matched_list[rider[0]] = driver[0]
                # kafka_matched_sink = format_message_matched(
                #     rider[0], rider[1], rider[2], rider[3], driver[0], driver[1], driver[2], distance, str(datetime.now()))
                # sink_match.append(kafka_matched_sink)
                kafka_driver_sink = format_message_driver(
                    driver[0], rider[2], str(datetime.now()))
                sink_driver.append(kafka_driver_sink)
                matched_driver[driver[0]] = "new"

        # print("raxit stop", line[1])

    # dont need this computation since we can figureout unmatched riders by using the matched riders and total stats
    # for key in matched_list:
    #     # print("raxit: iterating key", key)
    #     if key not in total_ride_req:
    #         # print("raxit:appending key")
    #         unmatched_rider_list.append(key)

    # don't require this computation coz we already know the matched driver from matched rides
    # for key in matched_driver:
    #     if key not in total_driver:
    #         unmatched_driver_list.append(key)

    # if len(matched_list) != 0:
    # print("inserting value:", len(matched_list))
    matched_stats = format_match_stats(len(total_ride_req), len(
        matched_list), len(total_driver), str(datetime.now()))
    # print(matched_stats)
    kafkaSink(matched_stats)

    # print("total number of ride request in a window: ", len(total_ride_req))
    # print("Ride requests matched with driver in a window: ", len(matched_list))
    # print("total number of driver active in the window: ", len(total_driver))
    # print("number of drivers matched with rider in the window: ", len(matched_driver))

    # print(len(total_ride_req), len(matched_list))
    # print(len(total_driver), len(matched_driver))
    # print(len(sink_match), len(sink_driver))
    # print('--------------------')
    print('total Driver:', len(total_driver))
    print('total ride req:', len(total_ride_req))


def main():

    #initializing the Spark Context
    sparkContext = SparkContext(appName='Bipartite-Matching')
    sparkContext.setLogLevel('ERROR')
    sparkStreamingContext = StreamingContext(sparkContext, 1)

    # create DStream that reads the Driver Stream
    spark_kafka_driver_Stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['driver_topic'],
                                                              # {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                              {'metadata.broker.list': 'localhost:9092'})
    
    #creating DStream that reads the Rider stream
    spark_kafka_rider_stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['rider_topic'],
                                                             #  {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                             {'metadata.broker.list': 'localhost:9092'})

    
    # defining the Window size
    driver_window = spark_kafka_driver_Stream.window(2)
    rider_window = spark_kafka_rider_stream.window(4)


    # creating location hash - precision 0.5 on driver RDD.
    driver_window = driver_window.map(lambda x: x[1])\
        .map(lambda x: x.split(";"))\
        .map(lambda x: (geohash(x[1]), x))
    # print(driver_window.count())

    # optional debugging: checking the counts of driver RDD
    driver_count = driver_window.foreachRDD(
        lambda x: print('driver:', x.count()))

    # creating location hash - precision 0.5 on rider RDD.
    rider_window = rider_window.map(lambda x: x[1])\
        .map(lambda x: x.split(";"))\
        .map(lambda x: (geohash(x[1]), x))

    # optional debugging: checking the counts of Rider RDD
    rider_count = rider_window.foreachRDD(lambda x: print('rider:', x.count()))


    # Geerdy match - left outer join on Driver RDD and Rider RDD on key location hash.
    union_rdd = rider_window.leftOuterJoin(driver_window)

    # optional debugging: mantaining the count for Joined RDD
    join_count = union_rdd.foreachRDD(lambda x: print('join:', x.count()))

    # union_rdd = union_rdd.foreachRDD(
    #     lambda rdd: rdd.foreachPartition(process_union))

    
    # optional Debugging: running without partitioning RDDs.
    union_rdd = union_rdd.foreachRDD(lambda x: process_union(x))

    
    sparkStreamingContext.start()
    sparkStreamingContext.awaitTermination()


if __name__ == '__main__':
    main()
