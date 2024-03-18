#include <stdio.h>
int main(){
	double a[] = {0.1,0.5,0.7,0.2};
	int elementNumbersOf_a=4;
	double d=0;
	printf("array originale : ");
	printArrayElement(a,elementNumbersOf_a);
	array_quadro(a,elementNumbersOf_a);
	printf("\narray quadrato : ");
	printArrayElement(a,elementNumbersOf_a);
}

int somma_quadrata(int a, int b){ //Questi parametri sono passati localmente e vengono allocati sullo stack
	a*=a;
	b*=b;
	return a+b;
}

void array_quadro(double a[],unsigned int n){ 
//Gli array sono SEMPRE passati per riferimento, si passa il puntatore al primo elemento e la lunghezza dell'array
	for (int i=0;i<n;i++){
		a[i]*=a[i];
	}
	//Questa funzione modifica l'array, non ritorna nulla, modifica il parametro passato
}

void printArrayElement(double a[],unsigned int n){
	printf("\n");
	for (int i=0;i<n;i++){
		printf("%lf  ",a[i]);
	}
}

//Se voglio passare una variabile per riferimento devo passare il puntatore
void test(int *a){
	
}
