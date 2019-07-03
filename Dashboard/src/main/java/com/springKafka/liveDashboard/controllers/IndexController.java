package com.springKafka.liveDashboard.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
@RequestMapping("/")
public class IndexController {
	@GetMapping("/index")
	public String index(Model model) {
		String[] cmd = { "sh", "/home/ubuntu/UMatch/run.sh" };
		// String[] cmd2 = { "sh", "/home/ubuntu/UMatch/run-kafka.sh" };
		// String driver = "/home/ubuntu/UMatch/kafka-injestion/driver-injestion.py &";
		// String rider = "/home/ubuntu/UMatch/kafka-injestion/rider-injestion.py &";
	

		try {

			// Restart the Pipeline

			Process p = Runtime.getRuntime().exec(cmd);
			//Process p2= Runtime.getRuntime().exec(cmd2);
			// Runtime.getRuntime().exec(driver);
			// Runtime.getRuntime().exec(rider);
			System.out.println("raxit executed the shell command");

			Thread.sleep(5000);



		} catch (Exception e) {

			System.out.println("not able to start the Pipeline");

		}
		return "index";
	}
}
