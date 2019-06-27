from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def main():

    spark = SparkSession \
        .builder \
        .appName("structed streaming matching") \
        .getOrCreate()

    # sparkContext = SparkContext("local[2]", appName='Bipartite-Matching')
    # sparkContext.setLogLevel('ERROR')
    # sparkStreamingContext = StreamingContext(sparkContext, 1)

    df_driver = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "[localhost:9092]") \
        .option("subscribe", "driver-topic") \
        .load()
    df_driver.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

    # consoleoutput = df_driver.writeStream.outputMode("append").format("console").start()

    struct_driver = StructType([
        StructField("driver_id", StringType(), True),
        StructField("driver_loc", StringType(), True),
        StructField("water_mark_driver", TimestampType(), True)])

    # struct = StructType().add("driver_id",DataType.simpleString).add("driver_loc", DataType.simpleString).add("water_mark", DataType.simpleString)

    # df_driver_with_watermark = df_driver.select(from_json("value", struct_driver).alias("driver"))

    df_driver_with_watermark = df_driver.select(
        from_json(col("value").cast("string"), schema=struct_driver).alias("driver"))
    df_driver_with_watermark = df_driver_with_watermark.selectExpr(
        "driver.driver_id", "driver.driver_loc", "driver.water_mark_driver")
    # df_driver_with_watermark = df_driver_with_watermark.withColumn("water_mark_driver",to_timestamp("water_mark_driver"))

    wc = df_driver_with_watermark.select(
                explode(
                    split(df_driver_with_watermark.filter,";")
                ).alias("word")
    )

    wordcount = wc.groupBy('word').count()  
    # df_driver_with_watermark.printSchema()

    # df_driver_with_watermark = df_driver_with_watermark.select('driver_id')

    # df_driver_with_watermark.writeStream.start()

    # df_join = df_driver_with_watermark\
    #     # .withWatermark("water_mark_driver", "20 seconds")\
    #         .groupBy(
    #             # window("water_mark_driver","5 seconds", "10 second"),
    #             "driver_id"
    #         ).count()

    # df_join = df_driver_with_watermark.groupBy("driver_id").count()

    # spark.streams.awaitAnyTermination()

    # schema = StructType().add("driver_id", StringType()).add("driver_loc", StringType()).add("water_mark", StringType())
    # df_driver.select(
    # col("key").cast("string"),
    # from_json(col("value").cast("string"), schema))

    # df_rider = spark \
    #     .readStream \
    #     .format("kafka") \
    #     .option("kafka.bootstrap.servers", "[localhost:9092]") \
    #     .option("subscribe", "rider-topic") \
    #     .load()
    # df_rider.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

    # struct_rider = StructType([
    #     StructField("ride_req_id", StringType(), True),
    #     StructField("pickup_loc", StringType(), True),
    #     StructField("dropoff_loc", StringType(), True),
    #     StructField("water_mark_rider", TimestampType(), True)])

    # df_rider_with_watermark = df_rider.select(
    #     from_json(col("value").cast("string"), schema=struct_rider).alias("rider"))

    # df_rider_with_watermark = df_rider_with_watermark.selectExpr(
    #     "rider.ride_req_id", "rider.pickup_loc", "rider.dropoff_loc", "rider.water_mark_rider").withWatermark("water_mark_rider", "10 seconds")
    # df_rider_with_watermark.show()

    # # op = df_driver_with_watermark.select("driver_id")

    # # op.writeStream.format("console").option("truncate", "false").start().awaitAnyTermination()

    # # UMatch = df_rider_with_watermark.join(
    # #     df_driver_with_watermark,
    # #     expr("""
    # #         water_mark_rider = water_mark_driver OR
    # #         water_mark_rider > water_mark_driver OR
    # #         water_mark_rider < water_mark_driver
    # #     """)
    # # )

    # output = df_driver_with_watermark.writeStream.outputMode("append").format("kafka").option(
    #     "checkpointLocation", "/tmp/checkpoint").start()
    # output.pprint()

    df_driver_with_watermark.writeStream.format("console").start()
    
    # # rider_join = df_rider_with_watermark.withWatermark("water_mark_rider", "20 seconds")

    # # op = driver_join.writeStream.outputMode("complete").format("console").start()
    # # op.awaitTermination()

    # # print("raxit")
    # # driver_join.isStreaming()
    # # df_driver.printSchema()
    # # print(df_driver[2])
    # # joined = rider_window.join(driver_window,
    # #                            expr("""
    # #                                 water_mark = water_mark
    # #                                 water_mark >= water_mark AND

    # #                                 """),
    # #                            "leftOuter")

    # # joined.isStreaming()

    # # value schema: { "a": 1, "b": "string" }
    # # schema = StructType().add("driver_id", StringType()).add("driver_loc", StringType()).add("water_mark", StringType())
    # # df.select(
    # # col("key").cast("string"),
    # # from_json(col("value").cast("string"), schema))

    # # df.selectExpr("driver_id","driver_loc", "water_mark")
    # # print("raxit this is schema:")
    # # df.printSchema()


if __name__ == "__main__":
    main()
