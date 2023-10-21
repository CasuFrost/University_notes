package EserciziCapitolo3;

public class Card {
	private String type;
	private String suit;
	public String card;
	public Card(String stringCard) {
		StringToTypes(stringCard);
		card = type.concat(suit);
	}
	
	public String getDescription() {
		String cardDescritpion="";
		switch(type) {
		case "1":
			cardDescritpion="One";
			break;
		case "2":
			cardDescritpion="Two";
			break;
		case "3":
			cardDescritpion="Three";
			break;
		case "4":
			cardDescritpion="Four";
			break;
		case "5":
			cardDescritpion="Five";
			break;
		case "6":
			cardDescritpion="Six";
			break;
		case "7":
			cardDescritpion="Seven";
			break;
	
		case "8":
			cardDescritpion="Eight";
			break;
		case "9":
			cardDescritpion="Nine";
			break;
		case "10":
			cardDescritpion="Ten";
			break;
		case "J":
			cardDescritpion="Jack";
			break;
		case "Q":
			cardDescritpion="Queen";
			break;
		case "K":
			cardDescritpion="King";
			break;
		case "A":
			cardDescritpion="Ace";
			break;
		default:
			cardDescritpion="?";
			break;

		}
		switch(suit) {
		case "S":
			cardDescritpion=cardDescritpion.concat(" of Swords");
			break;
		case "H":
			cardDescritpion=cardDescritpion.concat(" of Hearth");

			break;
		case "D":
			cardDescritpion=cardDescritpion.concat(" of Diamonds");

			break;
		case "C":
			cardDescritpion=cardDescritpion.concat(" of Spades");
			break;
		default :
			cardDescritpion=cardDescritpion.concat("?");
			break;
		}
		return cardDescritpion;
		
	}
	private void StringToTypes(String s) {
		String[] a = s.split("(?!^)");
		
		if(s.length()==3) {
			type = a[0];
			suit = a[1].concat(a[2]);
		}else {
			type = a[0];
			suit = a[1];
		}
		
	}
}
