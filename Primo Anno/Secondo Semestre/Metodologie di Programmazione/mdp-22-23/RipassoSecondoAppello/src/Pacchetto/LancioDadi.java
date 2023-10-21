package Pacchetto;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
public class LancioDadi {
	public static void execute() throws FileNotFoundException {
		Random r = new Random();
		int[] lanci = new int[20];
		HashMap<Integer,Integer> occ = new HashMap<>();
		
		occ.put(0, 1);
		lanci[0] = r.nextInt(6)+1;
		int lastInd=0;
		for(int i = 1;i<20;i++) {
			lanci[i]=r.nextInt(6)+1;
			if(lanci[i]==lanci[i-1]) {
				int tmp=occ.get(lastInd);
				occ.put(lastInd, tmp+1);
			}else {
				lastInd=i;
				occ.put(i, 1);
			}
		}
		int maxOccInd=0;
		for(Integer i : occ.keySet()) {
			if(occ.get(i)>occ.get(maxOccInd)) {
				maxOccInd=i;
			}
		}
		int n = -1;
		System.out.print("\n");
		for(int i = 0;i<20;i++) {
			if(i==maxOccInd) {
				System.out.print("(");
				n = lanci[i];
			}
			if(n>=0 &&n!=lanci[i]) {
				n=-1;
				System.out.print(")");
			}
			System.out.print(lanci[i]);
		}
		HashSet<String> occ2 = new HashSet<>();
		occ.get(0);
		
		System.out.println();
		PriorityQueue q = new PriorityQueue();
		
		q.add("PROVA");
		q.add("PROVA2");
		q.add("PROVA3");
		q.add("PROVA4");
		System.out.println(q.toString());
		q.poll();
		System.out.println(q.toString());
		
		
		
		PrintWriter writer = new PrintWriter("a.txt");
		writer.print("porcaccioddio");
		writer.close();
		
		

		
		
		
		
		
		
	}
}
