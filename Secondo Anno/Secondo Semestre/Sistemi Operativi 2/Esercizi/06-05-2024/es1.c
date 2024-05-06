#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void start()
{
    int i = 20;
    while (i > 0)
    {
        printf("TIMER : %d\n", i);
        sleep(1);
        i--;
    }
}

int main(int argc, char *argv[])
{

    pthread_t tid;

    pthread_create(&tid, 0, start, NULL);

    pthread_join(tid, (int *)&argc);

    return EXIT_SUCCESS;
}