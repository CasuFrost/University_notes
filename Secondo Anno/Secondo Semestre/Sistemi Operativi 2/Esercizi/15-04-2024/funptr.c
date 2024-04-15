#include <stdio.h>
#include <stdlib.h>

void fun1()
{
	printf("Sono fun1()\n");
}

void fun2()
{
	printf("Sono fun2()\n");
}

void main()
{
	int n;
	void (*funptr)(); // puntatore a funzione senza valori di ritorno

	if (scanf("%d", &n) < 1)
	{ // legge un intero da stdin
		printf("\nErrore nella lettura\n");
		exit(1);
	}

	switch (n)
	{
	case 1:
		funptr = fun1;
		break;
	case 2:
		funptr = fun2;
		break;
	default:
		printf("\nOpzione sconosciuta\n");
		exit(1);
	}

	(*funptr)(); // chiama la funzione scelta dall'utente
	exit(0);
}
