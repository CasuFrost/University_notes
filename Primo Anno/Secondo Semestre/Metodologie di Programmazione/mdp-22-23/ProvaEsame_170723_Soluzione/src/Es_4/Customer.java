package Es_4;

import java.util.Scanner;

/**
 * L'implementazione assume che, nel caso in cui il subtotale superi almeno 100$, venga applicato uno sconto di 10$ sull'
 * acquisto seguente.
 */
public class Customer {
	private double total;
	private static double discountTally;

	public void makePurchase(double amount) {
		if (discountReached()) {
			total = total + amount - 10.0;
			discountTally = amount - 10.0;
		} else {
			total = total + amount;
			discountTally = discountTally + amount;
		}
	}

	public boolean discountReached() {
		if (discountTally >= 100) {
			return true;
		} else {
			return false;
		}
	}

	public double getTotal() {
		return total;
	}

	// Only for evaluation purposes
	public void run_es4() {
		boolean done = false;
		discountTally = 0;
		Customer c = new Customer();
		while (!done) {
			Scanner in = new Scanner(System.in);
			System.out.println("Please enter a purchase amount, -1 to quit: ");
			double input = in.nextDouble();

			if (input == -1) {
				done = true;
			} else {
				c.makePurchase(input);
			}
		}

		System.out.println("Total sale, including discounts : " + c.getTotal());
	}
}