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

	void *m1 = malloc(size);
	void *m2 = malloc(size);

	if(m1==NULL || m2==NULL){
		printf("errore allocazione\n");
		exit(1);
	}

	FILE* fp;

	fp = fopen(argv[2],"r");

	if(fp==NULL){
		printf("errore apertura file\n");
		exit(1);
	}




	
	return 0;
}
