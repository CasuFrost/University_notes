#include <stdio.h>

long int fact(long int n)
{
    if (n == 0)
    {
        return 1;
    }
    return n * fact(n - 1);
}

int main()
{
    printf("%ld", fact(20));
}