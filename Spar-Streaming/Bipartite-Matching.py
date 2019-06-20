from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import expr
from pyspark.streaming.kafka import KafkaUtils
# import psycopg2
# from configparser import ConfigParser


def Joining_streams(driver_window, rider_window):

    print(driver_window)    
    print(rider_window)

    return 0


def main():

    sparkContext = SparkContext("local[2]", appName='Bipartite-Matching')
    sparkContext.setLogLevel('ERROR')
    sparkStreamingContext = StreamingContext(sparkContext, 1)
    # kafka_params = config('kafka')
    # create DStream that reads from kafka topic
    spark_kafka_driver_Stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['driver_topic'],
                                                              {'metadata.broker.list': 'localhost:9092'})

    spark_kafka_rider_stream = KafkaUtils.createDirectStream(sparkStreamingContext, ['rider_topic'],
                                                             {'metadata.broker.list': 'localhost:9092'})

    # driver_rdd = spark_kafka_driver_Stream.map(lambda line: line[1].split(";"))

    # driver_rdd.pprint()

    driver_window = spark_kafka_driver_Stream.window(20)
    rider_window = spark_kafka_rider_stream.window(60)

    # driver_window = spark_kafka_driver_Stream.withWatermark("water_mark", "2 hours")
    # rider_window = spark_kafka_rider_stream.withWatermark("water_mark","20 seconds")

    # joined_stream = Joining_streams(driver_window, rider_window)

    # driver_data_stream.foreachRDD(lambda rdd: rdd.foreachPartition(process_driver_messages))

    sparkStreamingContext.start()
    sparkStreamingContext.awaitTermination()


if __name__ == '__main__':
    main()
