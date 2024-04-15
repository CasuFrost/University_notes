#include <stdio.h>

static void fun()
{
	static int myvar;

	myvar++;
	printf("myvar = %d\n", myvar);
}

void main()
{

	// printf("%3d", 'à');
	fun();
	exit(0);
}
