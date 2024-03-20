#include <stdio.h>
#include "leggi.h"
#include "checkIfPal.h"

 int main(){

    char str[MAX];

    int charLetti=leggi(str);

    if(!checkIfPal(str,charLetti)){
        printf("è palindroma\n");
        return 0;
    }
    printf("non è palindroma\n");
 }