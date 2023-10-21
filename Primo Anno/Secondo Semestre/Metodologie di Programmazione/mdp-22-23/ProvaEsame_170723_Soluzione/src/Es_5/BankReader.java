package Es_5;

import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;

/**
 * This program prompts the user to enter a file name with account information.
 * A bank object is filled with the account numbers and balances specified in
 * the file. In case of an exception, the user can choose another file.
 */
public class BankReader {
	public void run_es5() {
		boolean done = false;
		Scanner in = new Scanner(System.in);

		while (!done) {
//         System.out.print("Filename: ");
//         String filename = in.next();
			String filename = "src/Es_5/input.dat";

			try {
				Bank bank = new Bank();
				bank.readFile(filename);

				System.out.println("Account with the highest balance");
				BankAccount highest = bank.getHighestBalance();
				System.out.println(highest.toString());

				System.out.println("\n");
				float avg = bank.getAverageBalance();
				System.out.println("Average balance: " + avg);

				System.out.println("\n");
				System.out.println("List of all accounts with a negative balance:");
				ArrayList<BankAccount> negativeAccounts = bank.getNegativeBalanceAccounts();
				for (BankAccount b : negativeAccounts) {
					System.out.println(b.toString());
					System.out.println("\n");
				}

				done = true;
			} catch (IOException e) {
				System.out.println(e);
			}
		}
	}
}
