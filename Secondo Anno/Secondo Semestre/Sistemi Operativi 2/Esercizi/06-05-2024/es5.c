#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int myVar = 0;

void incrementa(int i)
{
    int add = i * 10 - 14;
    printf("incremento di %d\n", add);
    myVar += add;
}

void start()
{
    for (int i = 0; i < 10; i++)
    {
        incrementa(i);
    }
}

int main(int argc, char *argv[])
{

    pthread_t tid;

    pthread_create(&tid, 0, start, NULL);

    for (int i = 0; i < 10; i++)
    {
        incrementa(i);
    }

    pthread_join(tid, (int *)&argc);

    printf("La variabile assume valore %d\n", myVar);

    return EXIT_SUCCESS;
}