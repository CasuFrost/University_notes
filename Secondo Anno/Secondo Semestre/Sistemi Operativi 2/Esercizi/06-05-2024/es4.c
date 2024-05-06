#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int m = 1049;

void start(int n)
{
    printf("la somma è %d", n + m);
}

int main(int argc, char *argv[])
{

    pthread_t tid;
    if (argc < 2)
    {
        printf("passare un argomento in input\n");
        exit(1);
    }
    pthread_create(&tid, 0, start, atoi(argv[1]));

    pthread_join(tid, (int *)&argc);

    return EXIT_SUCCESS;
}