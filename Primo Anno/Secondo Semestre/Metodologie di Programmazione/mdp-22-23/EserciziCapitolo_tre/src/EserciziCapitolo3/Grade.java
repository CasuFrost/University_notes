package EserciziCapitolo3;

public class Grade {
	private String letterGrade;

	public String getLetterGrade() {
		return letterGrade;
	}
	public float getNumericGrade(String letterGrade) {
		String[] b = letterGrade.split("(?!^)");
		float NumericGrade=0;

		String carattere = b[0].toString();
		switch(carattere) {
		case "A":
			NumericGrade=4;
			break;
		case "B":
			NumericGrade=3;
			break;
		case "C":
			NumericGrade=2;
			break;
		case "D":
			NumericGrade=1;
			break;
		case "F":
			NumericGrade=0;
			break;
		default:
			NumericGrade= -1;
			break;
		}
		float plus = 0;
		if(b.length>1) {
			
			if(!carattere.equals("F")) {
				if (b[1].equals("+")) {
					plus+=0.3;
				}else {
					plus-=0.3;
				}
			}else {
				return -1;
			}
		}
		if(NumericGrade+plus>4) {
			return 4.0f;
		}else {
			return NumericGrade+plus;
		}
		
	}
	public void setLetterGrade(String letterGrade) {
		this.letterGrade = letterGrade;
	}
	
	public String getConvertedLetterGrade(double i) {
		int intpart = (int)i;
		double decpart = i-intpart;
		String vote = "";
		if(i>=0 && i<0.5) {
			vote="F";
		}
		if(i>=0.5 && i<1.5) {
			vote="D";
		}
		if(i>=1.5 && i<2.5) {
			vote="C";
		}
		if(i>=2.5 && i<3.5) {
			vote="B";
		}
		if(i>=3.5) {
			vote="A";
		}
		
		if(decpart<=0.5 && decpart>=0.15) {
			vote=vote.concat("+");
			
		}
		if(decpart<=0.85 && decpart>=0.5) {
			vote=vote.concat("-");
			
		}
		
		return vote;
	}
	
	

}
