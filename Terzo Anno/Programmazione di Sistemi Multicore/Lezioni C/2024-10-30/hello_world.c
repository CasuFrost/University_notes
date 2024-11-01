#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define THREAD_COUNT 6

void *Hello(void *rank)
{
    int my_rank = rank;

    printf("hello from thread %ld\n", my_rank);
    return NULL;
}

int main()
{
    pthread_t thread_handles[THREAD_COUNT];

    for (int i = 0; i < THREAD_COUNT; i++) /*creazione dei thread*/
    {
        pthread_create(&thread_handles[i], NULL, Hello, (void *)i);
    }

    printf("hello from main thread\n");

    for (int i = 0; i < THREAD_COUNT; i++) /*terminazione dei thread*/
    {
        pthread_join(thread_handles[i], NULL);
    }

    return 0;
}