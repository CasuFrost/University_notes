#include <stdio.h>

int main(){

    //Si può aprire un file dichiarando una variabile puntatore ad un file
    //La funzione fopen ritorna un puntatore ad un FILE

    FILE *fp;

    fp=fopen("../Esercizi/27-03-2024/file2.txt","r");

	if ( fp == NULL ){ 
		printf("--> errore di apertura");
		exit(1);
	}

    char line[50];
    fgets(line,50,fp);

    printf("%s",line);

    return 0;
}