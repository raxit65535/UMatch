from __future__ import print_function
from kafka import KafkaProducer
import boto3
from smart_open import smart_open
import numpy
import random
from datetime import datetime
import re



# formatting the message to produce the record
def format_message(driver_id, driver_loc, water_mark_driver):
    str_fmt = "{};{};{}"
    message = str_fmt.format(driver_id, driver_loc, water_mark_driver)
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

    # Iterating over each files in the Bucket
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

            if firstline:  # skip first line
                firstline = False
                continue

            line_split = line.decode('utf8').split(",")

            # selecting the only records which has Pickup location and drop off location
            # making the Drop off location as Driver's current location and producing the record. Encoding UTF8
            if len(line_split) < 20:  
                continue
            if line_split[5] == '0' or line_split[6] == '0' or line_split[7] == '0' or line_split[8] == '0':
                continue
            else:
                driver_loc = (float(line_split[7]), float(line_split[8]))

                # Generating a Random Driver ID
                driver_id_verbose = 'driver:' + \
                    str(datetime.now()) + ":" + str(random.randint(1, 1000))
                
                # Trimming the Driver ID
                driver_id = re.sub('[\W\_]', '', driver_id_verbose)
                
                # formatting the message {}
                formatted_message = format_message(
                    driver_id, driver_loc, str(datetime.now()))

                # producting the message
                producer.send('driver_topic',
                              formatted_message.encode('utf8 '))


if __name__ == '__main__':
    main()
