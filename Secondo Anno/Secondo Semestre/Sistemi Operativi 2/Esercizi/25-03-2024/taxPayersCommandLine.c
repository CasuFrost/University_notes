#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "taxPayers.h"

// Prototipo Funzione newTP
taxpayer_t *newTP(char *, long int, float, birthdate_t);

int main(int argc, char *argv[])
{

    taxpayer_t *p1;

    float taxBalance, netIncome;
    birthdate_t date = {atoi(argv[4]), atoi(argv[5]), atoi(argv[6])};

    p1 = newTP(argv[1], atoi(argv[2]), atof(argv[3]), date);

    taxBalance = p1->income * p1->taxRate;
    netIncome = (*p1).income - taxBalance; // oppure netIncome= p1->income - taxBalance;

    printf("ID: %s, taxBalance: %f net: %f\n", p1->ID, taxBalance, netIncome);

    printf("BD = %d/%d/%d\n", (*p1).bd.year, (*p1).bd.month, (*p1).bd.day);

    free(p1);
}
