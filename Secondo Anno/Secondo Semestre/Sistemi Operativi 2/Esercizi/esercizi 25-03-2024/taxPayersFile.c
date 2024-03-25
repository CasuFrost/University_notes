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
    birthdate_t date = {2022, 1, 1};

    p1 = newTP("CSAKJS18R17U813F", 5000, 0.25, date);

    taxBalance = p1->income * p1->taxRate;
    netIncome = p1->income - taxBalance; // oppure netIncome= p1->income - taxBalance;

    printf("ID: %s, taxBalance: %f net: %f\n", p1->ID, taxBalance, netIncome);

    printf("BD = %d/%d/%d\n", (*p1).bd.year, (*p1).bd.month, (*p1).bd.day);

    free(p1);
}
