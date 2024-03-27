#include <stdio.h>
int main(){
	system("clear");
	
	
	punto2();
}

void punto1(){
	
	int array[] = {1,4,6,7,3,1,4,5,6,7,8,4,3,2,9};

	int byte = sizeof(array[0]);
	int lenght = sizeof(array) / byte;
	
	
	printf("Che numero si vuole cercare?");
	int k;
	scanf("%d",&k);
	int f=0;
	int i = 0;
	for(;i<lenght;i++){
		if(k==array[i]){
			f=1;
			break;
		}
	}
	if(f) {printf("trovato, si trova nella posizione %d\n",i+1);}
	else{printf("non è nell'array");}
}

void punto2(){
	printf("Inserire lunghezza dell'array (massimo 10 numeri) : \n");
	int n;
	do{
		scanf("%d",&n);
	}while(n<1 || n>10);
	
	float values[n];
	
	for(int i=0;i<n;i++){
		printf("\nInserire il valore %d : ",i+1);
		scanf("%d",&values[i]);
	}
	
	float sum=0;
	
	for(int i=0;i<n;i++){
		sum = sum+values[i];
	}
	
	printf("\nLa media aritmetica è %f",sum/n);
	
}
