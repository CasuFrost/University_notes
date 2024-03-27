#include <stdio.h>

#define MAX 10

void main() {
    int nc = -1;
    char str[MAX+1];        // un char in piu' per '\0'

    // lettura (bufferizzata) da stdin
    // scrive direttamente nella stringa
    while ((str[++nc] = getchar()) != EOF) ;

    /* 
    // vediamo cosa c'e' nella stringa
    for (int i = 0; i < MAX+1; i++)
        printf("carattere = %d\n", str[i]);
    */

    // scrive '\0' a fine stringa
    str[(nc > MAX) ? MAX : nc] = '\0';

    printf("nc = %d; str = %s\n", nc, str);
}
