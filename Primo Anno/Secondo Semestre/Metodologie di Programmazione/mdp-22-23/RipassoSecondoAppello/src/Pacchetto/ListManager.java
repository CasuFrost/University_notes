package Pacchetto;


import java.io.PrintWriter;
import java.io.IOException;
import java.util.*;
public class ListManager {
	ArrayList<Persona> list = new ArrayList<>();
	HashMap<String,ArrayList<String>> courseMap = new HashMap<>();
	public ListManager(ArrayList<Persona> in) {
		list = in;

		updateCourseMap();
		
	}
	public void addPerson(Persona p) {
		list.add(p);
		updateCourseMap();
	}
	private void updateCourseMap() {
		courseMap.clear();
		
		for(Persona  p : list) {
			
			ArrayList<String> tmp;
			if(courseMap.containsKey(p.getCourse())) {
				tmp = courseMap.get(p.getCourse());
			}else {
				tmp = new ArrayList<>();
			}
			
			String s = p.getName()+" "+p.getSurName();
			tmp.add(s.replace("_", " "));
			courseMap.put(p.getCourse(),tmp );
		}
	}
	public HashMap<String,ArrayList<String>> getCourseMap(){
		return courseMap;
	}
	public float avgAge() {
		int sum = 0;
		int cnt = 0;
		for(Persona  p : list) {
			sum+=p.getAge();
			cnt++;
		}
		return sum/cnt;
	}
	
	public void printCourseMapOnFile(String path) {
		try {
			PrintWriter w = new PrintWriter(path);
			for(String s : courseMap.keySet()) {
				w.print(s+" : [");
				for(String ss : courseMap.get(s)) {
					w.print(" "+ss+" ");
				}
				w.print("]\n");
			}
			w.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	
}
