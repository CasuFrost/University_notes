#include <stdio.h>


void increment(int *); // dichiaro il prototipo della funzione. Se non lo faccio mi da warning ... ma funziona

int main() {

	int n;
	int *nptr;

	n=5;
	nptr = &n;
	
	printf("n = %d, &n = %p nptr= %p, *nptr=%d, \n", n, &n, nptr, *nptr);
	
	*nptr=*nptr+1; //come scrivere n=n+1
	// in questo caso *nptr e' il simbolo (alias) che identifica la locazione di memoria memorizzata in nptr e' come se fosse un alias per  la variabile n;
		

	increment(&n);
	printf("n = %d \n",n);

	return 0;
}

void increment(int *num) {
	*num += 1; // or (*num)++;
} 




