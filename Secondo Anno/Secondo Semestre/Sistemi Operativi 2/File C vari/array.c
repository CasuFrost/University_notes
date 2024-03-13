#include <stdio.h>

int main(){

	// Occupano una regione contigua di memoria
	// La dimensione di un array rimane inalterata una volta definiti
	// Sono indicizzati da un intero positivo 
	
	unsigned int data[3]; //Array di 3 numeri interi
	
	/* Quando si dichiara un array è buona norma usare le costanti per la lunghezza, è  
	buona nominare le costanti con lettere maisucole */
	
	const unsigned int GIORNI = 365; 
	double temp_max[GIORNI];
	
	temp_max[0] = 1;
	
	//oppure 
	
	#define GIORNI_preprocessore 365
	double temp_max_prep[GIORNI_preprocessore];
	
	//La variabile temp_max è un puntatore al primo elemento dell'array
	
	//è possibile inizializzare gli array
	int g[300] = {2,5,7}; 
	//g[0] = 2, g[1] = 5,    g[2] = 7. 
	//Tutti gli elementi non inizializzati sono inizializzati a zero.
	
	//è possibile fare array multidimensionali (matrici)
	
	#define MESI 12
	#define GIORNI_M 31
	double giorno[MESI][GIORNI];
	
	int spazio = sizeof(temp_max); // dimensione dell'array : 365 (posizioni) * spazio che occupa un double = 365*8=2920
	printf("%d",spazio);
	
	for(int i = 0;i<2*GIORNI;i++) //Provando a scrivere oltre l'area di memoria allocata, l'OS potrebbe abortire il processo.
		temp_max[i]=0.0;
	
}
