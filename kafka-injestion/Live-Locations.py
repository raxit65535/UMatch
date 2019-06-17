from __future__ import print_function
from kafka import KafkaProducer
import boto3
from smart_open import smart_open
import numpy
from configparser import ConfigParser



def format_message(driver_loc, rider_loc):
    str_fmt = "{};{};{};{}"
    message = str_fmt.format(driver_loc[0],
                             driver_loc[1],
                             rider_loc[0],
                             rider_loc[1])
    # print(message)
    return message


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
                driver_loc = (float(line_split[5]),float(line_split[6]))
                print("driver",driver_loc)
                rider_loc = (float(line_split[7]), float(line_split[8]))
                print("rider",rider_loc)
                formatted_message = format_message(driver_loc,rider_loc)
                
                print("both",formatted_message)
                producer.send('driver_topic', formatted_message.encode('utf8 '))
                

if __name__ == '__main__':
        main()