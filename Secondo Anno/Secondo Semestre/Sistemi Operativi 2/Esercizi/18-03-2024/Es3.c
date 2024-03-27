#include <stdio.h>
#include <string.h>

int main(){ 
	char str1[] = "Ciao mondo";
	char str2[] = "impossibile";

	strncpy(str1,str2,5);
	//printf("%s\n",str1);

	char str3[] = "è una brava persona";
	char str4[] = "bianchi ";
	strncat(str4,str3,strlen(str3)+strlen(str4));
	printf("%s\n",str4);


	char str5[] = "sdfzdaaf";
	char str6[] = "asdfasfdas";

	
	getMinString(str5,str6);

	
	return 0;
}

void getMinString(char str5[]  ,char str6[]){
	

	if(strlen(str5)<strlen(str6)){
		printf("la minore è la prima\n");
		return;
	} 
	printf("la minore è la seconda\n");

}

