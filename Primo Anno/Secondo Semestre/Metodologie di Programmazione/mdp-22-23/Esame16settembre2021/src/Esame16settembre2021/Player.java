package Esame16settembre2021;

public class Player {
	private int cod;
	private String name;
	private String surname;
	private int age;
	public Player(int c,String n,String s,int a) {
		cod=c;
		age=a;
		name=n;
		surname=s;
	}
	public String getName() {return name+" "+surname;}
}
