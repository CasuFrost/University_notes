#include <stdio.h>
int main(){ 
	int i = -1;
	{int i=1;
	for (;i < 3; i++)
		printf("i = %d\n", i);
	}
	printf("i = %d\n", i);
	return 0;
}
