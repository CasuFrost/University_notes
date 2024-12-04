#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#define THREAD_NUM 4

void *thread_func(void *n)
{
    printf("hi im thread %d\n", (int)n);
}

int main(int argc, char **argv)
{
    pthread_t tids[THREAD_NUM];
    for (int i = 0; i < THREAD_NUM; i++)
    {
        pthread_create(&tids[i], NULL, thread_func, (void *)i);
    }
    for (int i = 0; i < THREAD_NUM; i++)
    {
        pthread_join(tids[i], NULL);
    }
}