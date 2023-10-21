package Esame;

public class Esercizio3 {
	public void Exe() {
		System.out.println("ESERCIZIO 3");
		Customer customer = new Customer();
		customer.setAvailableDiscount(1);
		double amount=95;
		System.out.println("FASE 1 - l'utente ha già uno sconto, fa un aquisto compreso tra 90 e 100 euro :");
		
		System.out.println("SITUAZIONE PRE ACQUISTO");
		System.out.println("Soldi accumulati prima di ricevere uno sconto : "+ customer.getSoldiSpesi());
		System.out.println("Sconti disponibili : "+ customer.getAvailableDiscount());
		
		System.out.println("SITUAZIONE POST ACQUISTO DAL VALORE DI "+amount);
		
		customer.makePurchase(amount);
		
		System.out.println("Soldi accumulati prima di ricevere uno sconto : "+ customer.getSoldiSpesi());
		System.out.println("Sconti disponibili : "+ customer.getAvailableDiscount());
		System.out.println("");
		
		System.out.println("FASE 2 - l'utente non ha sconti, ma fa un acquisto in modo tale da poterne ottenere uno :");
		amount=34;
		System.out.println("SITUAZIONE PRE ACQUISTO");
		System.out.println("Soldi accumulati prima di ricevere uno sconto : "+ customer.getSoldiSpesi());
		System.out.println("Sconti disponibili : "+ customer.getAvailableDiscount());
		customer.makePurchase(amount);
		System.out.println("SITUAZIONE POST ACQUISTO DAL VALORE DI "+amount);
		System.out.println("Soldi accumulati prima di ricevere uno sconto : "+ customer.getSoldiSpesi());
		System.out.println("Sconti disponibili : "+ customer.getAvailableDiscount());
	
		for(int i=0;i<50;i++) {
			System.out.print("-");
		}
		System.out.println("");
	}
}
