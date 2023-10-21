package Esame19maggio2021;
import java.util.*;

public class AirportGateManager {
	ArrayList<Plane> allPlanes = new ArrayList<Plane>();
	Queue<Plane> takeOffQueue = new LinkedList<Plane>();
	Queue<Plane> landQueue = new LinkedList<Plane>();
	
	TreeSet<String> k = new TreeSet<>();
	HashSet<String> kk = new HashSet<>();

	
	public boolean takeOff(int cod) {
		for(int i=0;i<allPlanes.size();i++) {
			if(allPlanes.get(i).getCod()==cod) {
				takeOffQueue.add(allPlanes.remove(i));
			}
		}
		return true;
	}
	public boolean land(int cod) {
		for(int i=0;i<allPlanes.size();i++) {
			if(allPlanes.get(i).getCod()==cod) {
				landQueue.add(allPlanes.remove(i));
			}
		}
		return true;
	}
	public boolean next() {
		if(landQueue.size()!=0) {
			allPlanes.add(landQueue.poll());
		}else if(takeOffQueue.size()!=0){
			allPlanes.add(takeOffQueue.poll());
			
		}else {
			System.out.println("Non ci sono azioni disponibili");
		}
		return true;
	}
	public boolean quit() {
		return false;
	}
	
}
