package EserciziCapitolo_11;
import java.io.FileReader;

import java.io.FileNotFoundException;

import java.io.PrintWriter;

import java.util.*;
 
public class Main {

	public static void main(String[] args)throws FileNotFoundException {
		
		Random r = new Random();
		r.nextInt(21);
		System.out.println(r.nextInt(21)+1);
		HashMap dict = new HashMap();
		dict.put("nome", 5);
		dict.put("soldi", 6);
		dict.put("fama", 6);
		
		ArrayList a = new ArrayList();
		TreeSet<String> u = new TreeSet<String> ();
		
		
		u.add("ciao");
		u.add("ciao");
		u.add("ciaoz");
		Iterator k = u.iterator();
		while(k.hasNext()) {
			System.out.println(k.next());
		}
		
		System.out.println(5+"a");
		Iterator it = dict.keySet().iterator();
		Iterator it2 = dict.keySet().iterator();
		while(it2.hasNext()) {
			Object t = it2.next();
			dict.replace(t, (int)dict.get(t)+3);
		}
		while(it.hasNext()) {
			System.out.println(dict.get(it.next()));
		}
		
		
		//Esercizio 1
		Esercizio1 es1 = new Esercizio1();
		//es1.Exe();
		
		//Esercizio 2
		Esercizio2 es2 = new Esercizio2();
		//es2.Exe();
		
	}

}
