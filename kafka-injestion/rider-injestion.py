from __future__ import print_function
from kafka import KafkaProducer
import boto3
from smart_open import smart_open
import numpy, random, re
from datetime import datetime
# from configparser import ConfigParser



def format_message(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider):
    str_fmt = "{};{};{};{}"
    message = str_fmt.format(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider)
    # print(message)
    return message

def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1), numpy.linspace(p1[1], p2[1], parts+1))


def main():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('nyc-tlc')
   
    producer = KafkaProducer(bootstrap_servers = "localhost:9092")

    for obj in bucket.objects.filter(Prefix="trip data"):
        key = obj.key
        print(key)
       
        if key.startswith('trip data/fhv'):
            continue

        #building absolute file name
        file_name = 's3://nyc-tlc/' + key
        #skipping header
        firstline = True
        # Processing each row in file
        for line in smart_open(file_name):

            # print(line.decode('utf8'))
            if firstline:  # skip first line
                firstline = False
                continue

            line_split = line.decode('utf8').split(",")
            if len(line_split) < 20: #Skipping rows with large number of columns
                continue
            if line_split[5] == '0' or line_split[6] == '0' or line_split[7] == '0' or line_split[8] == '0':
                continue
            else:
                pickup_loc = (float(line_split[5]),float(line_split[6]))
                # print("driver",driver_loc)
                drop_off_loc = (float(line_split[7]), float(line_split[8]))
                # print("rider",rider_loc)
                ride_request_id_verbose = 'ride:' + str(datetime.now()) + ":" + str(random.randint(1, 10000))

                ride_request_id = re.sub('[\W\_]','',ride_request_id_verbose)

                intermediate_points = getEquidistantPoints(pickup_loc, drop_off_loc, 100)

                formatted_message = format_message(ride_request_id,pickup_loc, drop_off_loc, str(datetime.now()))
                


                print(formatted_message)
                producer.send('rider_topic', formatted_message.encode('utf8 '))

                # for int_point in intermediate_points:
                #     # print(int_point)
                #     ride_request_id_verbose = 'ride:' + str(datetime.now()) + ":" + str(random.randint(1, 10000))

                #     ride_request_id = re.sub('[\W\_]','',ride_request_id_verbose)
                #     formatted_message = format_message(ride_request_id,int_point, drop_off_loc, str(datetime.now()))

                #     producer.send('rider_topic', formatted_message.encode('utf8 '))                

if __name__ == '__main__':
        main()