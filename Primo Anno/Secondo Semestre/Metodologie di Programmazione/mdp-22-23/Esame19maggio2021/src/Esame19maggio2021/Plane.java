package Esame19maggio2021;

import java.io.FileNotFoundException;

public class Plane {
	private boolean flying;
	private int cod;
	public Plane(int c) {
		cod=c;
		flying=false;
	}
	public void land() {
		flying=false;
	}
	public void takeOff() {
		flying=true;
	}
	public int getCod() {return cod;}
	
}
