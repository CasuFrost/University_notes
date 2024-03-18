#include <stdio.h>


int main() {

	int vect[10];
	int *ptr=NULL, *ptr1=NULL;
	int i;

	ptr=&vect[0];
	ptr1=vect;	

	printf(" ptr = %p\n ptr1 = %p\n", ptr, ptr1);
	i=0;
	do{
		*ptr = i;
		ptr++; i++;
	} while (ptr<=&vect[10]); //perche' sappiamo che un vettore e' allocato in celle di memoria contigue!!!

	ptr=vect;
	for (i=0; i<10; i++) {
		printf("ptr = %p, *ptr = %d \n", ptr, *ptr);
		ptr++;
	}

	printf(" vect[10] = %d  *(vect + 10) =  %d \n",  vect[10], *(vect + 10) );

	

	return 0;
}






