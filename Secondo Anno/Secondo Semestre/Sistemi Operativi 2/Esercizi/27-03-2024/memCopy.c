#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 50

int main(int argc, char *argv[])
{
	int size = 1;
	if (argc != 1)
	{
		size = atoi(argv[1]);
	}
    int ogSize=size;

	char *m1 = malloc(size);
	char *m2 = malloc(size);

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

    int lenght=0;
    char line[MAX_LINE];
    int offset=0;

    char ch=fgetc(fp);
    while ( ch != EOF){

        lenght = strlen(line);
        
       
        size+=lenght;
        realloc(m1,lenght);
        

        for(int i=0;i<lenght;i++){
            m1[i+offset]=line[i];
        }

        offset+=lenght;
        char ch=fgetc(fp);

    }

    for(int i=0;i<size;i++){
            printf("%c",m1[i]);
    }

	
    
	return 0;
}
