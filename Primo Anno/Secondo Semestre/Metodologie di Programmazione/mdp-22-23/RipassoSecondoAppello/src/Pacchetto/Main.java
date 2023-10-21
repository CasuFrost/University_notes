package Pacchetto;
import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws FileNotFoundException {
		System.out.println("Lista dei presenti : \n");
		File f = new File("listaDati.txt");
		Scanner in = new Scanner(f);
		
		ArrayList<Persona> persons = new ArrayList<>();
		while(in.hasNextLine()) {
			persons.add(new Persona(in.nextLine()));
		}
		
		ListManager listManager = new ListManager(persons);
		System.out.print(listManager.getCourseMap().toString());
		listManager.printCourseMapOnFile("courseMap.txt");
		
		LancioDadi.execute();
	}

}
