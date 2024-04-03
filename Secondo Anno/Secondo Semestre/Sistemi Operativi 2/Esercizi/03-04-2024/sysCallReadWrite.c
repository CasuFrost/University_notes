#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/fcntl.h>


#define MAX_LINE 50
#define MAX_FILESIZE 100

int min(int a,int b){
	if(a<b)return a;
	return b;
}

int main(int argc, char *argv[])
{
	int size = 1;
	if (argc != 1)
	{
		size = atoi(argv[1]);
	}
    int ogSize=size;

	char *m1 = malloc(size);

	if(m1==NULL){
		printf("errore allocazione\n");
		exit(1);
	}

    int fd = open(argv[2],O_RDONLY);

    if(fd==-1){
        printf("errore apertura file\n");
		exit(1);
    }

	FILE* fp = fopen(argv[2],"r");


	char ch=fgetc(fp);

	int i=0;
	while(ch!=EOF){
		if(i==size){
			size++;
			m1=realloc(m1,size);
		}
		m1[i]=ch;
		i++;
		ch=fgetc(fp);
	}
	printf("%d  %d",size,ogSize);

	if(fp==NULL){
        printf("errore apertura file\n");
		exit(1);
    }

    //read(fd,m1,size);

	int fd_out = open(argv[3],O_WRONLY|O_TRUNC);


	int fileSizeInByte=0;
	while(m1[fileSizeInByte]!='\0'){
		fileSizeInByte++;
	}


	write(fd_out,m1,min(fileSizeInByte,MAX_FILESIZE));

	close(fd);
	close(fd_out);
    
	return 0;
}

