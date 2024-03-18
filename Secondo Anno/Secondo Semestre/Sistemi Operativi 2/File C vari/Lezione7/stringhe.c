// STRINGHE

#include <stdio.h>
#include <string.h>  	//Libreria contenente funzioni e macro 
						//per la gestione delle stringhe


int main(int argc, char *args[])
{

// Diversi modi di inizializzare le stringhe

	char s[10];
	char s1[10]="Lezione 9";
	char s2[10]="L9 4apr";
	char s3[]="L9 4apr";
	char s4[10]={'L','9',' ','4','a','p','r'}; //Sconsigliato
	char s5[10]={'L','9',' ','4','a','p','r','\0'};


/* Le stringhe vanno gestite con funzioni dedicate:
 - size_t strlen(const char *s); 
lunghezza di una stringa

 - char *strcpy(char *dest, const char *src); 
copia della stringa src nella stringa dest

 - int strcmp(const char *s1, const char *s2);
confronta il contenuto di s1 con s2. Restituisce:
	0 	se s1==s2
	<0 	se s1<s2
	>0 	se s1 > s2

 - char *strcat(char *dest, const char *src);
concatena il contenuto della stringa src con quello di dest e mette la  nuova stringa  in dest

- char *gets(char *s); 
- char *fgets(char *s, int size, FILE *stream);
- int puts(const char *s);
*/

// Stampa  di una stringa
//	int puts (const char *strPtr);


//  LUNGHEZZA  DI  UNA  STRINGA

	printf("Lunghezza di s= %d\n",(int)strlen(s));
	printf("Lunghezza di s1= %d\n",(int)strlen(s1));
	printf("Lunghezza di s2= %d\n",(int)strlen(s2));
	printf("Lunghezza di s3= %d\n",(int)strlen(s3));
	printf("Lunghezza di s4= %d\n",(int)strlen(s4));
	printf("Lunghezza di s5= %d\n",(int)strlen(s5));
	
//  ASSEGNAZIONE  DI UN VALORE AD UNA STRINGA, OVVERO COPIA DI UNA STRINGA

	//s="Lezione 9"; //KO, illegale,  da  errore 
	strcpy(s,"Lezione 9");
	printf("Lunghezza di s= %d\n",(int)strlen(s));
	// oppure
	strcpy(s,s2);
	printf("Lunghezza di s= %d\n",(int)strlen(s));

//  CONFRONTO TRA STRINGHE

	if (s==s2) printf(" ==; le stringhe  sono uguali\n");
	else printf(" == con le stringhe  nn funziona\n");
	
	if (!strcmp(s,s2)) printf(" strcmp; le stringhe  sono uguali\n");
	else printf(" strcmp; le stringhe non sono uguali %d\n",strcmp(s,s1));

// CONCATENZAZIONE s1 +  s2

	char str[30]="Lezione 9";
	char str1[]="del 3 Aprile 2020";
	int l;
	l=(int)strlen(str);
	strcat(str,str1);
	printf("Lunghezza str=%d, str1=%d, str+str1=%d\n",l,(int)strlen(str1), (int)strlen(str));
	



	printf("s  = %s \n",s);	
	puts(s);

/*
	printf("s1 \n");
	puts(s1);
	printf("s2 \n");
	puts(s2);
	printf("s3 \n");
	puts(s3);
	printf("s4 \n");
	puts(s4);
	printf("s5 \n");
	puts(s5);
	printf("\n");

*/	


}



