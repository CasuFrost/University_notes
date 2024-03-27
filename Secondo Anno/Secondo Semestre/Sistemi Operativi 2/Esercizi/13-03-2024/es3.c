#include <stdio.h>
int main(){ 
	printf("enter a positive wight :\n");
	int w;
	scanf("%d",&w);
	while(w<=0){
		printf("\nenter a positive wight :\n");
		scanf("%d",&w);
	}
}

