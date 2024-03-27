#include <stdio.h>
#include <stdlib.h>

/*
	void *malloc(size_t size);
	void free(void *ptr);
	void *calloc(size_t nmemb, size_t size);

*/



int main() {

	char *strPtr=NULL;
	int *intPtr=NULL;
	const int SIZE_OF_ARRAY=30;	
	int i;

	strPtr=(char *) calloc(SIZE_OF_ARRAY, sizeof(char) );
	// (char *) indica il casting ad un puntatore di tipo char 
	// Perche' serve fare il casting?
	if (strPtr==NULL) exit(1);

	intPtr=(int *) calloc(SIZE_OF_ARRAY, sizeof(int));
	if (intPtr==NULL) exit(1);

	/* E' come se avessimo 2  array di dimensione SIZE_OF_ARRAY
	calloc inizializza il contenuto della memoria a 0
	*/

	// Accedere alla  memoria allocata  con aritmetica dei putatori
	for (i=0;i<SIZE_OF_ARRAY;i++) {
		printf("%c ",*(strPtr + i));
	}
	for (i=0;i<SIZE_OF_ARRAY;i++) {
		printf("%d ",*(intPtr + i));
	}

	//Accedere alla memoria allocata con la notazione degli array
		
	for (i=0; i<SIZE_OF_ARRAY; i++) {
		intPtr[i]=i;
	}
	for (i=0;i<SIZE_OF_ARRAY;i++) {
		printf("%d ",intPtr[i]);
	}
	
	free(intPtr);
	free(strPtr);

	return 0;
}






