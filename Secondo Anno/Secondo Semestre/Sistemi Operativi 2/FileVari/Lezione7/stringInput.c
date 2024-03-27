// STRINGHE I/O

#include <stdio.h>
#include <string.h>  	
#define MAX_LINE_LEN 80

int main(int argc, char *args[])
{

// Diversi modi di inizializzare le stringhe

	char s[10];
	char lineIn[80];
	int lineLen;
	char c;

/* INPUT */
	
	printf("Inserisci una stringa (gets)");
	gets(s);
	puts("s");
	puts(s);

	printf("Inserisci una stringa (fgets)");
	fgets(lineIn, MAX_LINE_LEN, stdin);
	lineLen=(int)strlen(lineIn);
//fgets inserisce \n+\0 alla fine  della stringa se MAX_LINE_LEN non raggiunto se non vogliamo \n lo possiamo rimuovere
	if (lineIn[lineLen-1]=='\n')  
		lineIn[lineLen-1]='\0';
	printf("lineLen = %d \n",lineLen);
	printf("Len. di lineIn = %d\n", (int)strlen(lineIn)); 

	printf("inserisci un carattere (getchar)\n");
	c=getchar();
	printf("hai inserito %c \n",c);

	return 0;
}



