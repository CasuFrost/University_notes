package Pacchetto;

public class Persona {
	private String name;
	private String surName;
	private String city;
	private int age;
	private String course;
	public Persona(String line) {
		String[] data = line.split(" ");
		name = data[0];
		surName=data[1];
		city = data[2];
		age = Integer.valueOf(data[3]);
		course = data[4];
	}
	public String getName() {
		return name;
	}
	public String getSurName() {
		return surName;
	}
	public String getCity() {
		return city;
	}
	public int getAge() {
		return age;
	}
	public String getCourse() {
		return course;
	}
}
