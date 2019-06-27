package com.springKafka.liveDashboard.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumerService{
	
	@Autowired
	SimpMessagingTemplate template;
	
	@KafkaListener(topics="${kafka.topic}")
	public void consume(@Payload String message) {
		
			String[] stats = message.split(";");

			System.out.println(stats[0]+"--->"+stats[1]);
			// this.template.convertAndSend("/topic/total_req", stats[0]);
			// this.template.convertAndSend("topic/matched_req", stats[1]);
			this.template.convertAndSend("/topic/location_hash", message);
	
		
	}

	// @KafkaListener(topics="${kafka.topic1}")
	// public void consume_location_hash(@Payload String message) {
		
	// 		String[] stats = message.split(";");

	// 		System.out.println("after Hashing"+stats[0]+"--->"+stats[1]);
	// 		// this.template.convertAndSend("/topic/total_req", stats[0]);
	// 		// this.template.convertAndSend("topic/matched_req", stats[1]);
	// 		this.template.convertAndSend("/topic/location_hash", message);
	
		
	// }
}
