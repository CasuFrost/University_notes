#include <stdio.h>


int main() {

	int n=5;
	int *nptr, *nptr1, *nptr2;

	nptr = &n;

	nptr1 = nptr+1;

	nptr2 = nptr+3; //3x4 = 12 = 0xC 

	printf(" nptr = %p\n nptr1 = %p\n nptr2 = %p \n", nptr, nptr1, nptr2);

/* As es:
 nptr  = 0x7fff829e3644 + 0x4 = 0x7fff829e3648
 nptr1 = 0x7fff829e3648 
 nptr  = 0x7fff829e3644 + 0xc
 					 45
					 46
					 ...
					 4F	   
 nptr2 = 0x7fff829e3650 
*/
	
	nptr2 -= 3;

	printf(" nptr2 = %p", nptr2);
		


	return 0;
}






