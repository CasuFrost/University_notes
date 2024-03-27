#include  <stdio.h>
#include  <string.h>
#include  <stdlib.h>

#define  MAX_LINE 100		// lunghezza massima di una linea

int main(int argc, char * argv[]) {

	char line[MAX_LINE];
	int line_l;
	FILE *fp;

	fp = fopen(argv[1],"r");
	if ( fp == NULL ){ 
		printf("--> errore di apertura");
		exit(1);
	}
    

	// COME FACCIO A LEGGERE TUTTO IL FILE?
	// IL FILE FINISCE QUANDO ARRIVO A EOF
	while ( fgets(line,MAX_LINE,fp) ){

		// toglie '\n' dalla fine della stringa
		line_l = strlen(line);
		if (line[line_l-1] == '\n')
			line[line_l-1] = '\0';

		// stampa la stringa e aggiunge '\n'
		puts(line);
	}

	// anche alla chiusura ci va il controllo
	if ( fclose(fp) != 0 ) {
		printf("--> errore in chiusura");
		exit(1);
	}
	return 0;
}
