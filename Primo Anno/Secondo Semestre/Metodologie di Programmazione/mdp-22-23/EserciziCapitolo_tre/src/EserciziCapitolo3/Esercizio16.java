package EserciziCapitolo3;
import java.util.*;
import java.math.*;
public class Esercizio16 {
	public void Do() {
		int a,b,c=0;
		System.out.println("ESERCIZIO 16 :");
		Scanner sc=new Scanner(System.in);
		System.out.println("Inserire primo valore :");
		a=sc.nextInt();
		System.out.println("Inserire secondo valore :");
		b=sc.nextInt();
		System.out.println("Inserire terzo valore :");
		c=sc.nextInt();
		int k = Math.max(a, b);
		System.out.println("il numero più grande è : ");
		System.out.print(Math.max(c, k));	
	}
}
