// STRINGHE I/O

#include <stdio.h>
#include <string.h>  	
#define MAX_LINE_LEN 80

int main(int argc, char *args[])
{

// Diversi modi di inizializzare le stringhe

	char s1[10]="Lezione 9";
	int i;

/*OUTPUT*/

	printf("s1 forward: %s\n",s1);
	
	printf("s1 backward: ");
	for (i=strlen(s1)-1; i>=0; i--) {
		putchar(s1[i]);
	}
	printf("\n");
	
	printf("puts(s1) equivale a printf(\"%%s\",s1)");
	puts("-"); //sostituisce il terminale \0 con \n	
	puts(s1);
	fputs(s1,stdout); //non aggiunge \n

	return 0;

}



