#include <stdio.h>
int main(){ 
	comb2();
	return 0;
}
void comb1(){
	system("clear");
	printf("Quanti dati si vogliono leggere? :\n");
	int n;
	scanf("%d",&n);
	int sum=0;
	int i = 0;
	while(i<n){
		int tmp=-1;
		
		while(1){
			printf("Inserire dato %d\n",i+1);
			scanf("%d",&tmp);
			if(!(tmp<=0 || tmp >=10)) break;
			printf("Valore fuori dal range!\n");
		}
		
		
		
		
		sum=sum+tmp;
		i++;
	}
	system("clear");
	printf("la somma è %d ed il valor medio è %d\n",sum,sum/n);
}

void comb2(){
	system("clear");
	printf("Quanti dati si vogliono leggere? :\n");
	int n;
	scanf("%d",&n);
	int sum=0;
	int i = 0;
	while(i<n){
		int tmp=-1;
		
		do{
			printf("Inserire dato %d\n",i+1);
			scanf("%d",&tmp);
			if(!(tmp<=0 || tmp >=10)) break;
			printf("Valore fuori dal range!\n");
		}while(1);
		
		
		
		
		sum=sum+tmp;
		i++;
	}
	system("clear");
	printf("la somma è %d ed il valor medio è %d\n",sum,sum/n);
}

void comb3(){
	system("clear");
	printf("Quanti dati si vogliono leggere? :\n");
	int n;
	scanf("%d",&n);
	int sum=0;
	for(int i=0;i<n;i++){
		int tmp=-1;
		
		while(1){
			printf("Inserire dato %d\n",i+1);
			scanf("%d",&tmp);
			if(!(tmp<=0 || tmp >=10)) break;
			printf("Valore fuori dal range!\n");
		}
		
		
		
		
		sum=sum+tmp;
	}
	system("clear");
	printf("la somma è %d ed il valor medio è %d\n",sum,sum/n);
}
