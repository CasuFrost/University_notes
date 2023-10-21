package Esame19maggio2021;
import java.io.*;

import java.util.*;
public class main {

	public static void main(String[] args) throws FileNotFoundException{
		//ESERCIZIO 3
		
		System.out.println("***********************ESERCIZIO 3***********************");
		//Leggo dal file ed inserisco nell'arrayList
		ArrayList<Raw> register = new ArrayList<>();
		File file = new File("input.txt");
		Scanner scanner = new Scanner(file);
		while(scanner.hasNextLine()) {
			Raw tmp = new Raw(scanner.nextLine());
			register.add(tmp);
		}
		HashMap dict = new HashMap();
		
		for(int i=0;i<register.size();i++) {
			if(dict.containsKey(register.get(i).getService())) {
				float tmp=0;
				tmp=(float)dict.get(register.get(i).getService());
				dict.put(register.get(i).getService(),tmp+  register.get(i).getAmount());
			}else {
				dict.put(register.get(i).getService(), register.get(i).getAmount());
			}
		}
		
		String max="";
		Float maxV=0f;
		Iterator i = dict.keySet().iterator();
		while(i.hasNext()) {
			String a = (String)i.next();
			float importo=(float)dict.get(a);
			System.out.println(a+", importo : "+importo);
		}
		
		
		
		
		ArrayList prova = new ArrayList();
		prova.add(1);
		prova.add("a");
		
		
	}
}
