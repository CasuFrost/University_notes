package Es_3;

public class Es_3 {

	public static void RisolviEsercizio() {
		int num_esecuzioni_corpo = 0;
		// A
		for (int i = 2; i <= 9; i++) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("a) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// B
		num_esecuzioni_corpo = 0;
		for (int i = 0; i < 10; i++) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("b) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// C
		num_esecuzioni_corpo = 0;
		for (int i = 10; i > 0; i--) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("c) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// D
		num_esecuzioni_corpo = 0;
		for (int i = -10; i >= 0; i++) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("d) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// E
		num_esecuzioni_corpo = 0;
		for (int i = -2; i >= 0; i++) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("e) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// F
		num_esecuzioni_corpo = 0;
		for (int i = -8; i <= 3; i = i + 4) {
			num_esecuzioni_corpo++;
		}
		
		System.out.println("f) Numero esecuzioni corpo:" + num_esecuzioni_corpo);

		// G
		num_esecuzioni_corpo = 0;
		for (int k = 0; k < 20; k += 2) {

			if (k + 3 == 1) {
				System.out.println(k + " ");
			}

			num_esecuzioni_corpo++;
		}
		
		System.out.println("g) Numero esecuzioni corpo:" + num_esecuzioni_corpo);
	}

}
