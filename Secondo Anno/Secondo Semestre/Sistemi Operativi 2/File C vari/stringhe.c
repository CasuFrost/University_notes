#include <stdio.h>

#include <string.h>  	//Libreria contenente funzioni e macro per la gestione delle stringhe

int main(){
    //Una stringa è un array di caratteri
    //Una stringa in C è sempre terminata dal carattere "\0"

    //Inizializzazione : 
    char s[10]="Lezione 7";
    /*
    I caratteri sono : 
    L - e - z - i - o - n - e -   - 7 - \0  
    */
    
    char s2[10] = "L7 3Apr" //I caratteri non inizializzati sono indefiniti, il carattere nullo alla fine è aggiunto

    //è possibile non definire la lunghezza della stringa, viene calcolata automaticamente 
    
    char s3[] = "Lezione Del Giorno"



}