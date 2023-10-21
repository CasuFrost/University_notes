package EserciziCapitolo_11;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class Esercizio1 {
	public void Exe() throws FileNotFoundException {
		FileReader reader = new FileReader("input.txt");
		Scanner in = new Scanner(reader);
		while(true) {
			try {
				System.out.println(in.nextLine());
			}catch(Exception e) {
				break; //Non trova una linea e chiude il programma
			}
		}
}
}
