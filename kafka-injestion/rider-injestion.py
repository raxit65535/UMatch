from __future__ import print_function
from kafka import KafkaProducer
import boto3
from smart_open import smart_open
import numpy
import random
import re
from datetime import datetime
# from configparser import ConfigParser

# generating synthetic ride requests


def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts+1), numpy.linspace(p1[1], p2[1], parts+1))


# formatting the message to produce the record
def format_message(ride_request_id, pickup_loc, drop_off_loc, water_mark_rider):
    str_fmt = "{};{};{};{}"
    message = str_fmt.format(ride_request_id, pickup_loc,
                             drop_off_loc, water_mark_rider)
    # print(message)
    return message


def main():
    # declaring the boto3 S3 resource
    s3 = boto3.resource('s3')

    # Defning the AWS S3 open dataset NYC Taxi Rides bucket
    bucket = s3.Bucket('nyc-tlc')

    # Defining the kafka producer - P.S. pip3 install kafka
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    # producer = KafkaProducer(
    #     bootstrap_servers="10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092")

    while(True):
        for obj in bucket.objects.filter(Prefix="trip data"):
            key = obj.key

            if key.startswith('trip data/fhv'):
                continue

            # building absolute file name
            file_name = 's3://nyc-tlc/' + key
            # skipping header
            firstline = True
            # Processing each row in file
            for line in smart_open(file_name):

                # skip first line
                if firstline:
                    firstline = False
                    continue

                line_split = line.decode('utf8').split(",")

                # Selecting only records which has pickup location and drop off location
                if len(line_split) < 20:
                    continue
                if line_split[5] == '0' or line_split[6] == '0' or line_split[7] == '0' or line_split[8] == '0':
                    continue
                else:
                    pickup_loc = (float(line_split[5]), float(line_split[6]))

                    drop_off_loc = (float(line_split[7]), float(line_split[8]))

                    # Generating Random Ride Request ID
                    ride_request_id_verbose = 'ride:' + \
                        str(datetime.now()) + ":" + str(random.randint(1, 10000))
                    # trimming the Ride Request ID
                    ride_request_id = re.sub('[\W\_]', '', ride_request_id_verbose)

                    # formatting the produced message {}
                    formatted_message = format_message(
                        ride_request_id, pickup_loc, drop_off_loc, str(datetime.now()))

                    # calling creation of synthetic message creation.
                    intermediate_points = getEquidistantPoints(
                        pickup_loc, drop_off_loc, 100)

                    # producing the message
                    producer.send('rider_topic', formatted_message.encode('utf8 '))

                    # producing synthetic ride requests
                    for int_point in intermediate_points:
                        # print(int_point)
                        ride_request_id_verbose = 'ride:' + \
                            str(datetime.now()) + ":" + \
                            str(random.randint(1, 10000))

                        ride_request_id = re.sub(
                            '[\W\_]', '', ride_request_id_verbose)
                        formatted_message = format_message(
                            ride_request_id, int_point, drop_off_loc, str(datetime.now()))

                        producer.send(
                            'rider_topic', formatted_message.encode('utf8 '))


if __name__ == '__main__':
    main()
