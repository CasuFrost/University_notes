package EserciziCapitolo3;
import java.math.*;
public class StringSet {
	private String smallest;
	private String largest;
	private String middle;
	public StringSet(String a, String b, String c) {
		if (a.length()>b.length()) {
			if(b.length()>c.length()) {
				//a>b>c
				smallest=c;
				middle=b;
				largest=a;
			}else {
				//a>c>b
				smallest=b;
				middle=c;
				largest=a;
			}
		}else if(b.length()>a.length()) {
			if(a.length()>c.length()) {
				//b>a>c
				smallest=c;
				middle=a;
				largest=b;
			}else {
				//b>c>a
				smallest=a;
				middle=c;
				largest=b;
			}
		}else if(c.length()>a.length()){
			if(a.length()>b.length()) {
				//c>a>b
				smallest=b;
				middle=a;
				largest=c;
			}else {
				//c>b>a
				smallest=a;
				middle=b;
				largest=c;
			}
		}
	}
	public String getSmallest() {
		return smallest;
	}
	public void setSmallest(String smallest) {
		this.smallest = smallest;
	}
	public String getLargest() {
		return largest;
	}
	public void setLargest(String largest) {
		this.largest = largest;
	}
	public String getMiddle() {
		return middle;
	}
	public void setMiddle(String middle) {
		this.middle = middle;
	}
}
