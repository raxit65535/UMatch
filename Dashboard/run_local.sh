# python3 /home/raxit/workspace/Insight-DataEngineering/UMatch/kafka-injestion/driver-injestion.py &
pkill -f rider-injestion.py 
pkill -f driver-injestion.py 
# spark-class org.apache.spark.deploy.Client kill spark://10.0.0.4:7077 Bipartite-Matching
python3 /home/raxit/workspace/Insight-DataEngineering/UMatch/kafka-injestion/rider-injestion.py &
python3 /home/raxit/workspace/Insight-DataEngineering/UMatch/kafka-injestion/driver-injestion.py &
/home/raxit/BigData/spark-2.4.3-bin-hadoop2.7/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 /home/raxit/workspace/Insight-DataEngineering/UMatch/Spark-Streaming/BipartiteMatching.py &
#java -jar /home/ubuntu/UMatch/Dashboard/target/Dashboard-0.0.1-SNAPSHOT.jar &
