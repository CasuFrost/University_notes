package Es_5;

import java.util.Scanner;
import java.io.IOException;
import java.util.NoSuchElementException;

/**
 * A bank account has a balance that can be changed by deposits and withdrawals.
 */
public class BankAccount {
	private double balance;
	private int accountNumber;
	private String firstName;
	private String lastName;

	/**
	 * Constructs a bank account with a zero balance.
	 */
	public BankAccount() {
		accountNumber = 0;
		balance = 0;
		firstName = "";
		lastName = "";
	}

	/**
	 * Constructs a bank account with a given balance.
	 */
	public BankAccount(int anAccountNumber, double initialBalance, String firstName, String lastName) {
		this.accountNumber = anAccountNumber;
		this.balance = initialBalance;
		this.firstName = firstName;
		this.lastName = lastName;
	}

	/**
	 * Reads an account number and balance.
	 * 
	 * @param in the scanner
	 * @return true if the data was read false if the end of the stream was reached
	 */
	public void read(Scanner in) throws IOException {
		try {
			int accNum = in.nextInt();
			String firstName = in.next();
			String lastName = in.next();
			double bal = in.nextDouble();

			this.accountNumber = accNum;
			this.balance = bal;
			this.firstName = firstName;
			this.lastName = lastName;
		} catch (NoSuchElementException exception) {
			throw new IOException("Incompatible types on input.");
		}
	}

	/**
	 * Deposits money into the bank account.
	 * 
	 * @param amount the amount to deposit
	 */
	public void deposit(double amount) {
		balance = balance + amount;
	}

	/**
	 * Withdraws money from the bank account.
	 * 
	 * @param amount the amount to withdraw
	 */
	public void withdraw(double amount) {
		balance = balance - amount;
	}

	/**
	 * Gets the current balance of the bank account.
	 * 
	 * @return the current balance
	 */
	public double getBalance() {
		return balance;
	}

	/**
	 * Gets the account number of the bank account.
	 * 
	 * @return the account number
	 */
	public int getAccountNumber() {
		return accountNumber;
	}

	/**
	 * Gets the first name of the bank account owner.
	 * 
	 * @return the first name
	 */
	public String getFirstName() {
		return firstName;
	}

	/**
	 * Gets the last name of the bank account owner.
	 * 
	 * @return the first name
	 */
	public String getLastName() {
		return lastName;
	}

	@Override
	public String toString() {
		return "Account Number: " + this.accountNumber + "\nFirst Name: " + this.firstName + "\nLast Name: "
				+ this.lastName + "\nBalance: " + this.balance;
	}
}
