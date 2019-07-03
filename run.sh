ps -f -C python3 | grep driver-injestion.py | awk '{print $2}' | xargs kill -9 $2
ps -f -C python3 | grep rider-injestion.py | awk '{print $2}' | xargs kill -9 $2
#/usr/local/spark/bin/spark-class org.apache.spark.deploy.Client kill spark://10.0.0.4:7077 Bipartite-Matching
kill -9 $(jps | grep SparkSubmit | grep -Eo '[0-9]{1,7}')
python3 /home/ubuntu/UMatch/kafka-injestion/driver-injestion.py&
python3 /home/ubuntu/UMatch/kafka-injestion/rider-injestion.py&
/usr/local/spark/bin/spark-submit --master spark://10.0.0.4:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 /home/ubuntu/UMatch/Spark-Streaming/BipartiteMatching.py&
#java -jar /home/ubuntu/UMatch/Dashboard/target/Dashboard-0.0.1-SNAPSHOT.jar &
