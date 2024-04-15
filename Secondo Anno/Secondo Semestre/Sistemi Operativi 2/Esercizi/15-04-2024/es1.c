#include <stdio.h>
#include "myv.c"

void func1()
{

    extern int myvar;

    void nestfunc1()
    {
        printf("sono nestfunc1\n");
    }

    nestfunc1();
    myvar = 1;
}

int main(void)
{

    printf("myvar = %d\n", myvar);
    func1();
    printf("myvar = %d\n", myvar);

    return 0;
}