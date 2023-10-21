package Esame16settembre2021;
import java.io.*;
import java.util.*;
public class GameManager {
	ArrayList<Player> players = new ArrayList<Player>();
	int availableSeat;
	public GameManager(String path) {
		File f = new File(path);
		try {
			Scanner s = new Scanner(f);
			while(s.hasNextLine()) {
				String line[]=s.nextLine().split(";");
				Player tmp = new Player(Integer.parseInt(line[0]),line[1],line[2],Integer.parseInt(line[3]));
				players.add(tmp);
			}
			System.out.println("il gioco inizia con "+players.size()+" giocatori");
			availableSeat=players.size()-1;
		}catch(FileNotFoundException e){
			System.out.println("errore file");
		}
	}
	public void removePlayer() {
		Random rng = new Random();
		Player choosen = players.remove(rng.nextInt(players.size()));
		availableSeat--;
		System.out.println(choosen.getName()+" è stato eliminato");
	}
	public void round() {
		Random rng = new Random();
		int milliseconds = (rng.nextInt(20)+1)*1000;
		System.out.println("la musica inizia");
		try {
			Thread.sleep(1);//Al posto di 1, devi scrivere milliseconds, ho scritto 1 per non dover aspettare i secondi ogni volta
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		removePlayer();
	}
	public boolean finished() {
		return players.size()==1;
	}
	public void win() {
		System.out.println("ha vinto "+players.get(0).getName());
	}
}
