#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int size = 1;
	if (argc != 1)
	{
		size = atoi(argv[1]);
	}

	int *m1 = malloc(size);
	int *m2 = malloc(size);

	int index = 0;

	while (1) // Inserire intero positivo
	{

		if (index >= size)
		{
			m1 = realloc(m1, index);
			size++;
		}

		int i;
		scanf("%d", &i);
		m1[index] = i;

		index++;
		if (i == -1)
		{
			break;
		}
	}

	for (int i = 0; i < index - 1; i++)
	{
		printf("\nhai inserito : %d\n", *(m1 + i));
	}

	free(m1);
	free(m2);
	return 0;
}
