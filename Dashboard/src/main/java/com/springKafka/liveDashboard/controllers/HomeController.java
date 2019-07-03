package com.springKafka.liveDashboard.controllers;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import javax.validation.constraints.Null;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class HomeController {
	@GetMapping("/home")
	public String home(Model model) {
		String[] cmd = { "sh", "/home/ubuntu/UMatch/Dashboard/run.sh" };
	
		try {
			// Restart the Pipeline
			Process p = Runtime.getRuntime().exec(cmd);
			System.out.println("raxit executed the shell command");
			Thread.sleep(5000);
		} catch (Exception e) {

			System.out.println("not able to start the Pipeline");

		}
		return "home";
	}
}
