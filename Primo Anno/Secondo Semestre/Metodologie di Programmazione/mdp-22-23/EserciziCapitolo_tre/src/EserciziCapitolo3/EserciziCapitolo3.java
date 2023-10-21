package EserciziCapitolo3;
import java.math.*;

import java.io.*;
import java.util.*;
public class EserciziCapitolo3 {
	
	public static void main(String[] args) {
		/*Esercizio12 es12 = new Esercizio12();
		Esercizio13 es13 = new Esercizio13();
		Esercizio15 es15 = new Esercizio15();
		Esercizio16 es16 = new Esercizio16();
		Esercizio17 es17 = new Esercizio17();
		es12.Do();
		es13.Do();
		es15.Do();
		es16.Do();
		es17.Do();*/
		Stack s = new Stack();
		Queue ss = new LinkedList();
		
		Scanner tt = new Scanner(System.in);
	
		System.out.println(tt.nextLine());
		HashMap a = new HashMap();
		a.put("a", 1);
		a.put("b", 1);
		if(a.containsKey("a")) {
			int k = (int)a.get("a");
			a.put("a", k+1);
		}
		Iterator ii = a.keySet().iterator();
		while(ii.hasNext()) {
			a.put(ii.next(), 6);
		}
		System.out.println(a.entrySet());
		Queue as = new LinkedList();
		
		String in[] = "1365456434655554".split("");
		int maxRep = 0;
		int index = 0;
		int maxTmp=0;
		int tmpRep=0;
		
		for(int i = 0;i<in.length-1;i++) {
			int tmp = Integer.valueOf(in[i]);
			int next =Integer.valueOf(in[i+1]);
			if(tmp==next) {
				tmpRep+=1;
			}else {
				tmpRep=0;
			}
			if(tmpRep>maxRep) {
				maxRep=tmpRep;
				index=i;
			}
		}
		index+=1;
		String num=in[index];
		int j = index;
		while(in[j].equals(num)) {
			j--;
		}
		for(int i = 0;i<in.length;i++) {
			System.out.print(in[i]);
			if(i==j  ) {
				System.out.print("(");
			}
			if(i==index  ) {
				System.out.print(")");
			}
		}
		
		

		HashSet<String> hashSet = new HashSet<>(); //Si può fare uguale con TreeSet
		hashSet.add("ciao");
		hashSet.remove("ciao"); //Rimuove l'elemento passato come parametro se presente nel set
		
		Queue queue = new LinkedList(); //La coda è implementata con LinkedList
		queue.add(1);
		queue.add(2);
		queue.poll(); //Rimuoverà 1
		
		
		
		
		
		
		
		HashMap<String,Integer> hashMap = new HashMap<>();
		//Esempio di aggiornamento di un valore di un dizionario
		//Facciamo finta che si ha un dizionario con chiavi stringhe e valori interi :
		//Si vuole sommare 1 al valore della chiave : "Chiara"
		
		
		
		
		
	
		
	}
}
