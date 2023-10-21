package Esame;

public class Customer {
	int availableDiscount = 0;
	double soldiSpesi = 0;
	public void makePurchase(double amount) {
		while(availableDiscount>0 && amount>=10) {
			amount-=10;
			availableDiscount-=1;
		}
		soldiSpesi+=amount;
		while(discountReached(soldiSpesi)){
			
		}
	}
	public boolean discountReached(double s) {
		if(s>=100) {
			soldiSpesi-=100;
			availableDiscount+=1;
			return true;
		}else {
			return false;
		}
	}
	public int getAvailableDiscount() {
		return availableDiscount;
	}
	
	public double getSoldiSpesi() {
		return soldiSpesi;
	}
	public void setAvailableDiscount(int i) {
		availableDiscount=i;
	}
	
	
}
