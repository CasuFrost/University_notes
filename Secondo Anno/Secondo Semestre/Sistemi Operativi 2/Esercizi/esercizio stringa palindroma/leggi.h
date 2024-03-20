#include <stdio.h>

#define MAX 10

int leggi(char str[]) {
    int nc = -1;

    
    while ((str[++nc] = getchar()) != EOF) ;

    
    str[(nc > MAX) ? MAX : nc] = '\0';
    return nc;
    
}