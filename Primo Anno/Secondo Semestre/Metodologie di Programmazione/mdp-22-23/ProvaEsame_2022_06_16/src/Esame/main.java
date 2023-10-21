package Esame;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;



public class main {

	public static void main(String[] args) throws FileNotFoundException {
		// TODO Auto-generated method stub
		
		Esercizio3 es3 = new Esercizio3();
		es3.Exe();
		
		Esercizio4 es4 = new Esercizio4();
		es4.Exe();
		ArrayList<String> a = new ArrayList();
		a.add("a");
		a.add("diomai");
		a.add("sasbur");
		Iterator i = a.iterator();
		String res="";
		while(i.hasNext()) {
			res+=i.next();
			
		}
		String as[]=res.split("o");
		System.out.println(as[0]);
		
		
		
	}	
		

}
