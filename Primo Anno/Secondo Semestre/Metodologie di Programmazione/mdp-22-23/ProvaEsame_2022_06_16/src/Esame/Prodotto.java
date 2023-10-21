package Esame;

public class Prodotto {
	
	int codiceProdotto;
	String nomeProdotto;
	int quantità;
	double prezzoPerUnità;
	public Prodotto() {
		
	}
	public Prodotto(int cod, String name, int quant, double price) {
		codiceProdotto=cod;
		nomeProdotto=name;
		quantità=quant;
		prezzoPerUnità=price;
	}
	
	public int getCodiceProdotto() {
		return codiceProdotto;
	}
	public void setCodiceProdotto(int codiceProdotto) {
		this.codiceProdotto = codiceProdotto;
	}
	public String getNomeProdotto() {
		return nomeProdotto;
	}
	public void setNomeProdotto(String nomeProdotto) {
		this.nomeProdotto = nomeProdotto;
	}
	public int getQuantità() {
		return quantità;
	}
	public void setQuantità(int quantità) {
		this.quantità = quantità;
	}
	public double getPrezzoPerUnità() {
		return prezzoPerUnità;
	}
	public void setPrezzoPerUnità(double prezzoPerUnità) {
		this.prezzoPerUnità = prezzoPerUnità;
	}
}
