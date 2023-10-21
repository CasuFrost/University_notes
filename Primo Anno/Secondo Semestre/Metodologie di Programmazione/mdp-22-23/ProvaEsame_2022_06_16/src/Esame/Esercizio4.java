package Esame;

import java.io.FileReader;
import java.io.FileNotFoundException;
import java.util.*;

public class Esercizio4 {
	public void Exe() throws FileNotFoundException {
		System.out.println("ESERCIZIO 4");
		ArrayList<Prodotto> prodotti = new ArrayList();
		FileReader reader = new FileReader("listaProdotti.txt");
		Scanner in = new Scanner(reader);
		while(in.hasNextLine()) {
			String line = in.nextLine();
			prodotti.add(lineToProduct(line));
		}
		
		//Prodotto più costoso
		Prodotto expensive = new Prodotto(0,"a",0,0);
		for(int i=0;i<prodotti.size();i++) {
			if(prodotti.get(i).prezzoPerUnità>expensive.prezzoPerUnità) {
				expensive=prodotti.get(i);
			}
		}
		System.out.println("il prodotto più costoso è : "+expensive.nomeProdotto+" con un prezzo di "+expensive.prezzoPerUnità+" euro al pezzo.");
		System.out.println(" ");
		//Prezzo medio per ciascun prodotto
		for(int i=0;i<prodotti.size();i++) {
			double rapportoMat;
			if(prodotti.get(i).quantità!=0) {
				 rapportoMat = prodotti.get(i).prezzoPerUnità/prodotti.get(i).quantità;
				 String rapporto = String.valueOf(rapportoMat);
				 System.out.println("il prodotto : "+prodotti.get(i).nomeProdotto+" ha un prezzo medio di : "+rapporto);
			}else {
				System.out.println("il prodotto : "+prodotti.get(i).nomeProdotto+" ha un prezzo medio non disponibile data la mancanza del prodotto in magazzino ");
			}
		}
		System.out.println(" ");
		System.out.println("Lista prodotti esauriti : ");
		//prodotti esauriti
		for(int i=0;i<prodotti.size();i++) {
			if(prodotti.get(i).quantità==0) {
				System.out.println(prodotti.get(i).nomeProdotto);
			}
		}
		for(int i=0;i<50;i++) {
			System.out.print("-");
		}
		System.out.println("");
	}
	
	public Prodotto lineToProduct(String l) {
		String prod[]=l.split(" ");
		Prodotto p = new Prodotto(Integer.valueOf(prod[0]),prod[1],Integer.valueOf(prod[2]),Double.valueOf(prod[3]));
		return p;
	}
	
	
}
