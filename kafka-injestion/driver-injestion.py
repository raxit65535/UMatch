from __future__ import print_function
from kafka import KafkaProducer
import boto3
from smart_open import smart_open
import numpy
import random
from datetime import datetime
import re
# from configparser import ConfigParser


def format_message(driver_id, driver_loc, water_mark_driver):
    str_fmt = "{};{};{}"
    message = str_fmt.format(driver_id, driver_loc, water_mark_driver)
    # print(message)
    return message


def main():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('nyc-tlc')

    # producer = KafkaProducer(bootstrap_servers="localhost:9092")
    producer = KafkaProducer(
        bootstrap_servers="10.0.0.4:9092, 10.0.0.5:9092, 10.0.0.10:9092")

    for obj in bucket.objects.filter(Prefix="trip data"):
        key = obj.key
        print(key)

        if key.startswith('trip data/fhv'):
            continue

        # building absolute file name
        file_name = 's3://nyc-tlc/' + key
        # skipping header
        firstline = True
        # Processing each row in file
        for line in smart_open(file_name):

            # print(line.decode('utf8'))
            if firstline:  # skip first line
                firstline = False
                continue

            line_split = line.decode('utf8').split(",")
            if len(line_split) < 20:  # Skipping rows with large number of columns
                continue
            if line_split[5] == '0' or line_split[6] == '0' or line_split[7] == '0' or line_split[8] == '0':
                continue
            else:
                driver_loc = (float(line_split[7]), float(line_split[8]))
                # print("driver",driver_loc)
                # rider_loc = (float(line_split[7]), float(line_split[8]))
                # print("rider",rider_loc)

                driver_id_verbose = 'driver:' + \
                    str(datetime.now()) + ":" + str(random.randint(1, 1000))
                driver_id = re.sub('[\W\_]', '', driver_id_verbose)
                formatted_message = format_message(
                    driver_id, driver_loc, str(datetime.now()))

                print(formatted_message)
                producer.send('driver_topic',
                              formatted_message.encode('utf8 '))


if __name__ == '__main__':
    main()
