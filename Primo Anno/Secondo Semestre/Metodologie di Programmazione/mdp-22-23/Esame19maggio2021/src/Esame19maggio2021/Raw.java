package Esame19maggio2021;
import java.io.*;
import java.util.Scanner;
public class Raw {
	
	
	private String clientName;
	private String service;
	private float amount;
	private String timeStamp;
	public Raw(String c,String s,float a,String t) {
		clientName=c;
		service=s;
		amount=a;
		timeStamp=t;
	}
	
	public Raw(String line) {
		String[] splitted=line.split(";");
		if(splitted.length==4) {
			clientName=splitted[0];
			service=splitted[1];
			amount=Float.parseFloat(splitted[2]);
			timeStamp=splitted[3];
		}else {
			System.out.println("la riga  -"+line+"-  non ha il giusto formato, non verrà inserita");
		}
	}
	public String getClientName() {
		return clientName;
	}
	public String getService() {
		return service;
	}
	public float getAmount() {
		return amount;
	}
	public String getTimeStamp() {
		return timeStamp;
	}
}
