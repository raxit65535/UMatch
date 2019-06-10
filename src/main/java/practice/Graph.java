package practice;

import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.Cluster;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.kstream.Produced;
import io.kgraph.Edge;
import io.kgraph.GraphSerialized;
import io.kgraph.KGraph;
import io.kgraph.utils.KryoSerde;
import io.kgraph.utils.StreamUtils;

class Graph {

    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-Graph");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.Long().getClass().getName());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Long().getClass().getName());
        
        final StreamsBuilder builder = new StreamsBuilder();

        KTable<Long, Long> vertices = StreamUtils.tableFromCollection(builder, props, Serdes.Long(), Serdes.Long(),
                getLongLongVertices());

        KTable<Edge<Long>, Long> edges = StreamUtils.tableFromCollection(builder, props, new KryoSerde<>(),
                Serdes.Long(), getLongLongEdges());

        KGraph<Long, Long, Long> graph = new KGraph<>(vertices, edges,
                GraphSerialized.with(Serdes.Long(), Serdes.Long(), Serdes.Long()));

        KTable<Long, Long> outDegrees = graph.outDegrees();

        // String expectedResult = "1,2\n" + "2,1\n" + "3,2\n" + "4,1\n" + "5,1\n";

        outDegrees.toStream().to("graph-outdegree", Produced.with(Serdes.Long(), Serdes.Long()));

        final Topology topology = builder.build();
        System.out.println(topology.describe());
        final KafkaStreams streams = new KafkaStreams(topology, props);
        final CountDownLatch latch = new CountDownLatch(1);

        // attach shutdown handler to catch control-c
        Runtime.getRuntime().addShutdownHook(new Thread("streams-shutdown-hook") {
            @Override
            public void run() {
                streams.close();
                latch.countDown();
            }
        });

        try {
            streams.start();
            latch.await();
        } catch (Throwable e) {
            System.exit(1);
        }
        System.exit(0);
    }

    public static List<KeyValue<Long, Long>> getLongLongVertices() {
        List<KeyValue<Long, Long>> vertices = new ArrayList<>();
        vertices.add(new KeyValue<>(1L, 1L));
        vertices.add(new KeyValue<>(2L, 2L));
        vertices.add(new KeyValue<>(3L, 3L));
        vertices.add(new KeyValue<>(4L, 4L));
        vertices.add(new KeyValue<>(5L, 5L));

        return vertices;
    }

    public static List<KeyValue<Edge<Long>, Long>> getLongLongEdges() {
        List<KeyValue<Edge<Long>, Long>> edges = new ArrayList<>();
        edges.add(new KeyValue<>(new Edge<>(1L, 2L), 12L));
        edges.add(new KeyValue<>(new Edge<>(1L, 3L), 13L));
        edges.add(new KeyValue<>(new Edge<>(2L, 3L), 23L));
        edges.add(new KeyValue<>(new Edge<>(3L, 4L), 34L));
        edges.add(new KeyValue<>(new Edge<>(3L, 5L), 35L));
        edges.add(new KeyValue<>(new Edge<>(4L, 5L), 45L));
        edges.add(new KeyValue<>(new Edge<>(5L, 1L), 51L));

        return edges;
    }

}