package EserciziCapitolo_11;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Esercizio2 {
	public void Exe() throws FileNotFoundException {
		Scanner console = new Scanner(System.in);
		System.out.println("Si inserisca il nome del file che si vuole aprire (senza estensione) :");
		String userInput = console.next();
		String fileName = userInput+".txt"; //Prendo il nome del file da aprire dalla console
		String outputFileName = userInput+"_out"+".txt"; 
		
		String output="";
		FileReader reader = new FileReader(fileName); //Apro e leggo il file
		Scanner in = new Scanner(reader);
		ArrayList outputLines = new ArrayList(); //Linee da scrivere sul file
		while(true) {
			try {
				String tmp = in.nextLine();
				if(tmp.length()>0) {
					outputLines.add(tmp);
					
				}

			}catch(Exception e) {
				break; //Non trova una linea e chiude il programma
			}
		}
		PrintWriter out = new PrintWriter(outputFileName); //Per scrivere sul file
		for(int i=0;i<outputLines.size();i++) {
			System.out.println(outputLines.get(i));
			out.println(outputLines.get(i));
		}
		out.close();
	}
}
