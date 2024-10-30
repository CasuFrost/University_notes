#include <stdio.h>
#include <pthread.h>
#include <math.h>
#include <time.h>

int main(int argc, char **argv)
{
    int precision = 100;
    if (argc > 1)
        precision = atoi(argv[1]);
    int thread_numbers = 6;
    int tosses = thread_numbers * precision;

    pthread_t tids[thread_numbers];
    for (int i = 0; i < thread_numbers; i++)
    {
    }
}
