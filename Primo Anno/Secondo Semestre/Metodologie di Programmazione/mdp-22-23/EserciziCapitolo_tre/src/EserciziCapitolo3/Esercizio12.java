package EserciziCapitolo3;

public class Esercizio12 {
	public void Do() {
		System.out.println("ESERCIZIO 12 : ");
		Grade grade = new Grade();
		grade.setLetterGrade("B+");
		System.out.println(grade.getNumericGrade(grade.getLetterGrade()));
	}
}
