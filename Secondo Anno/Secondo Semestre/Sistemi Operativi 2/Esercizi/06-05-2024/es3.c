#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void start(struct TrheadAndMess *a)
{
}

struct TrheadAndMess
{
    int tNum;
    char message[150];
};

int main(int argc, char *argv[])
{

    pthread_t tid[5];

    for (int i = 0; i < 5; i++)
    {
        struct TrheadAndMess tmp = {i, "messaggio del thread"};

        pthread_create(&tid[i], 0, start, &tmp);

        pthread_join(tid[i], (int *)&argc);
    }

    return EXIT_SUCCESS;
}