package Esame16settembre2021;
import java.util.*;
import java.io.*;
public class main {
	public static void main(String[] args) throws FileNotFoundException {
		
		//ESERCIZIO 3
		System.out.println("*****************************ESERCIZIO 3*****************************");
		GameManager g = new GameManager("fileEs3.txt");
		while(!g.finished()) {
			g.round();
		}
		g.win();
		System.out.println("*****************************FINE ESERCIZIO 3*****************************");
		//ESERCIZIO 4
		System.out.println("*****************************ESERCIZIO 4*****************************");
		
		File f = new File("fileEs4input.txt");
		int totalWords=0;
		Scanner s = new Scanner(f); 
		PrintWriter fileW = new PrintWriter("fileEs4output.txt");
		TreeSet<String> uniqueWords = new TreeSet<String>();
		while(s.hasNext()) {
			uniqueWords.add(s.next());
			totalWords++;
		}
		Iterator it = uniqueWords.iterator();
		while(it.hasNext()) {
			fileW.println(it.next());
		}
		fileW.close();
		System.out.println("parole totali : "+totalWords+" parole uniche : "+uniqueWords.size());
		System.out.println("*****************************FINE ESERCIZIO 4*****************************");
	}
	
}
