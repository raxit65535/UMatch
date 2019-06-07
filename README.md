# UShare


## Project Idea

Provide solution for Ride sharing problem using Graph Algorithm.
Building the simplified Data pipeline using Kafka Streams
Kafka does not have default graph processing APIs unlike Spark GraphX and Flink Gelly.
Found one GitHub repo which has pre built version of graph algorithms based on Google pregel computation model. (https://github.com/rayokota/kafka-graphs.git)
I would like to contribute randomized maximum bipartite matching algorithm to the open source repo as part of the project


## Business Use case

Driver Rider matching in Ride sharing is one of the complex problems which qualifies as NP-Hard problem.
Minimizing the cost of computation & travel distance (driver) can benefit the organization.
Customizing open source frameworks is a legitimate use case for number of organizations.

## Engineering Challange

Kafka doesn't have built in Library for Streaming Graph processing. 
Using and customizing the open source library (not in incubation yet) 
There are blind spots in gathering the perect data. e.g. dirver's current location is not present in NYC Texi dataset

## Dataset

NYC Taxi Rides: https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_green.pdf

## Tech Stack

