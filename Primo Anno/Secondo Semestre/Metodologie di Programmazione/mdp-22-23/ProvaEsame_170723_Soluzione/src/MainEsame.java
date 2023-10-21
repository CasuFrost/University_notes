import java.util.ArrayList;
import Es_1.Automobile;
import Es_3.*;
import Es_4.*;
import Es_5.*;

public class MainEsame {

	public static void main(String[] args) {

		System.out.println("MDP Soluzione Esame 16 Giugno 2021\n\n");

		// Esercizio 1
		System.out.println("Esercizio 1:");
		Automobile automobile = new Automobile();
		System.out.println(automobile.toString());

		// Esercizio 3
		System.out.println("\n\nEsercizio 3:");
		Es_3.RisolviEsercizio();

		// Esercizio 4
		System.out.println("\n\nEsercizio 4:");
		Customer c = new Customer();
		c.run_es4();

		// Esercizio 5
		System.out.println("\n\nEsercizio 5:");
		BankReader br = new BankReader();
		br.run_es5();

	}

}
