from pyspark import SparkContext
from pyspark.streaming import StreamingContext
# from pyspark.sql.functions import expr
from pyspark.streaming.kafka import KafkaUtils
import sys
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
# import psycopg2
# from configparser import ConfigParser

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """

    # lonlat1 = lonlat1.strip("()").split(",")
    # lonlat2 = lonlat2.strip("()").split(",")

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



def format_message_matched(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider, driver_id, driver_loc, water_mark_driver, now_timestamp):
    str_fmt = "{};{};{};{};{};{};{};{};"
    message = str_fmt.format(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider, driver_id, driver_loc, water_mark_driver, now_timestamp)
    # print(message)
    return message

def format_message_driver(driver_id, driver_loc, water_mark_rider):
    str_fmt = "{};{};{}"
    message = str_fmt.format(driver_id, driver_loc, water_mark_rider)
    # print(message)
    return message


def process_union(rdd):
    matched_list = dict()
    matched_driver = dict()
    
    total_ride_req = dict()
    total_driver = dict()

    sink_match = list()
    sink_driver = list()

    unmatched_rider_list = []
    unmatched_driver_list = []
    # print("raxit start")
    for line in rdd:

        rider, driver = line[1]
        rider = rider.split(";")
        driver = driver.split(";")
        
        # a,b,c,d,e,f,g = line[:]
        # ride_id, ride_pickup, ride_dropoff, req_timestamp,a = rider
        # driver_id, driver_loc, driver_timestamp = driver
        # # driver_loc_temp = line[1].strip("()").split(",")
        # # driver_lon = driver_loc_temp[0]
        # # driver_lat = driver_loc_temp[1]
        
        ride_pickup = rider[1].strip("()").split(",")
        driver_loc = driver[1].strip("()").split(",")
        ride_long = ride_pickup[0]
        ride_lat = ride_pickup[1]
        driver_long= driver_loc[0]
        driver_lat = driver_loc[1]
        
        # driver_loc = line[1].strip("()").split(",")
        
        # # line.split(";")
        # # print(ride_req_id, driver_id)
        
        # print(ride_req_id, ride_pickup, ride_dropoff, req_timestamp,driver_id, driver_loc, driver_timestamp)
        # print(rider[0], driver[0])
        # print(a,b,c,d,e,f,g)

        if rider[0] not in total_ride_req:
            total_ride_req[rider[0]] = "new"

        if driver[0] not in total_driver:
            total_driver[driver[0]] = "new"

        if rider[0] not in matched_list and driver[0] not in matched_driver:
            # print("not yet matched")
            distance = haversine(ride_long, ride_lat, driver_long, driver_lat)
            if  distance >1 and distance < 3:
                # print("herversine true, adding the value")
                matched_list[rider[0]] = driver[0]
                kafka_matched_sink = format_message_matched(rider[0],rider[1],rider[2], rider[3], driver[0],driver[1],driver[2], str(datetime.now()))
                sink_match.append(kafka_matched_sink)
                kafka_driver_sink = format_message_driver(driver[0], rider[2], str(datetime.now()))
                sink_driver.append(kafka_driver_sink)
                matched_driver[driver[0]] = ""
    
        # print("raxit stop", line[1])
    for key in matched_list:
        # print("raxit: iterating key", key)
        if key not in total_ride_req:
            print("raxit:appending key")
            unmatched_rider_list.append(key)

    for key in matched_driver:
        if key not in total_driver:
            unmatched_driver_list.append(key)
    
    
    print(len(total_ride_req), len(matched_list))
    print(len(total_driver), len(matched_driver))

def main():

    sparkContext = SparkContext("local[2]", appName='Bipartite-Matching')
    sparkContext.setLogLevel('ERROR')
    sparkStreamingContext = StreamingContext(sparkContext, 1)
    # kafka_params = config('kafka')
    # create DStream that reads from kafka topic
    spark_kafka_driver_Stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['driver_topic'],
                                                                # {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                              {'metadata.broker.list': 'localhost:9092'})
    spark_kafka_rider_stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['rider_topic'],
                                                            #  {'metadata.broker.list': '10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092'})
                                                            {'metadata.broker.list': 'localhost:9092'})

    # driver_rdd = spark_kafka_driver_Stream.map(lambda line: line[1].split(";"))

    # driver_rdd.pprint()

    driver_window = spark_kafka_driver_Stream.window(10)
    rider_window = spark_kafka_rider_stream.window(20)

    # driver_window = spark_kafka_driver_Stream.withWatermark("water_mark", "2 hours")
    # rider_window = spark_kafka_rider_stream.withWatermark("water_mark","20 seconds")

    # joined_stream = Joining_streams(driver_window, rider_window)

    # parallel_driver = sparkContext.parallelize(driver_window)
    # parallel_rider = sparkContext.parallelize(rider_window)
    # keyfind = rider_window.join(driver_window,"timestamp",)
    # keyfind = keyfind.foreachRDD(Joining_streams(keyfind))
    # keyfind.pprint()

    # driver_rdd = spark_kafka_driver_Stream.map(lambda x: x[1].split(";"))
    # driver_rdd = driver_window.map(lambda x: x[1].split(";"))
        # .map(lambda x: x[1].split(","))

    # rider_rdd = spark_kafka_rider_stream.map(lambda x: x[1].split(";"))
    # rider_rdd = rider_window.map(lambda x: x[1].split(";"))


    union_rdd = rider_window.leftOuterJoin(driver_window)

    # union_rdd = rider_rdd.join(driver_rdd)
    # union_rdd = union_rdd.map(lambda x: x[1].row_input().split(";"))


    print(haversine(-73.93758392333984, 40.75828170776367,-73.93763732910156, 40.758270263671875))
    union_rdd = union_rdd.foreachRDD(lambda rdd: rdd.foreachPartition(process_union))
    # union_rdd.pprint()
    # joined_rdd = rider_rdd.join(driver_rdd)
    # joined_rdd = rider_window.join(driver_window)
    # joined_rdd = joined_rdd.map(lambda x: x[1].split(";"))

    # joined_rdd = rider_rdd.map(lambda x: (x[0],x[1],x[2])\
    #     .join(driver_rdd.map(lambda y:(y[0],y[1],y[2],y[3])))
    
    # joined_rdd = rider_window.leftOuterJoin(driver_window)
    # joined_rdd = rider_window.leftOuterJoin(driver_window)

    # process_joined_rdd = joined_rdd.flatmap(lambda (k,v) : v.s)
    # driver_matrix = driver_rdd.foreachRDD(lambda rdd: rdd.foreachPartition(process_driver_matrix))
    # # driver_matrix = driver_rdd.foreachRDD(process_driver_matrix)

    # rider_matrix = rider_rdd.foreachRDD(lambda rdd: rdd.foreachPartition(process_rider_matrix))
    # # driver_rdd.foreachRDD(process)
    
    # print(driver_matrix)
    # print(rider_matrix)

    
    # driver_window.pprint()
    # driver_data_stream.foreachRDD(lambda rdd: rdd.foreachPartition(process_driver_messages))

    sparkStreamingContext.start()
    sparkStreamingContext.awaitTermination()


if __name__ == '__main__':
    main()
