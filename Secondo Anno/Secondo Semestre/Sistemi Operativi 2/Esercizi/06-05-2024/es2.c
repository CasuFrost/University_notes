#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void start(int n)
{
    printf("sono il thread %d\n", n + 1);
}

int main(int argc, char *argv[])
{

    pthread_t tid[5];

    for (int i = 0; i < 5; i++)
    {
        pthread_create(&tid[i], 0, start, i);

        pthread_join(tid[i], (int *)&argc);
    }

    return EXIT_SUCCESS;
}