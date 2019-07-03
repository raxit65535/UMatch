pkill -f rider-injestion.py 
pkill -f driver-injestion.py 
/usr/local/spark/bin/spark-class org.apache.spark.deploy.Client kill spark://10.0.0.4:7077 Bipartite-Matching
python3 /home/ubuntu/UMatch/kafka-injestion/driver-injestion.py &
python3 /home/ubuntu/UMatch/kafka-injestion/rider-injestion.py &
/usr/local/spark/bin/spark-submit --master spark://52.41.192.216:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 /home/ubuntu/UMatch/Spark-Streaming/BipartiteMatching.py &
#java -jar /home/ubuntu/UMatch/Dashboard/target/Dashboard-0.0.1-SNAPSHOT.jar &
