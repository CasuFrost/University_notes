package Es_1;

public class Automobile extends Veicolo {

	private boolean avviata;

	public Automobile() {
		this.nome = "313";
		// Non è possibile accedere a velocità e accelerazione in quanto
		// attributi private della classe base.
	}

	public void avvia() {
		this.setAvviata(true);
	}

	public boolean isAvviata() {
		return avviata;
	}

	public void setAvviata(boolean avviata) {
		this.avviata = avviata;
	}

	@Override
	public String toString() {
		return "Nome automobile: " + this.nome;
	}
}