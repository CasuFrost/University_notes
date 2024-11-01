#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

unsigned precision = 100000; /*punti generati da ogni thread*/
const unsigned thread_number = 6;

unsigned total_tosses;
unsigned point_in_center = 0;

/*gestione accesso a variabili condivise*/
pthread_mutex_t mutex;

void *thread_function(void *arg_p)
{
    int local_circle_point = 0;
    for (int i = 0; i <= precision; i++)
    {
        double x = (double)rand() / RAND_MAX * 2.0 - 1.0;
        double y = (double)rand() / RAND_MAX * 2.0 - 1.0;
        if (x * x + y * y < 1)
        {
            local_circle_point++;
        }
    }

    pthread_mutex_lock(&mutex);
    point_in_center += local_circle_point;
    pthread_mutex_unlock(&mutex);
}

int main(int argc, char **argv)
{
    if (argc > 1)
    {
        precision = atoi(argv[1]);
    }

    total_tosses = precision * thread_number;
    pthread_mutex_init(&mutex, NULL);
    pthread_t tids[thread_number];

    for (int i = 0; i < thread_number; i++)
    {
        pthread_create(&tids[i], NULL, thread_function, NULL);
    }
    for (int i = 0; i < thread_number; i++)
    {
        pthread_join(tids[i], NULL);
    }

    double esteem = ((double)point_in_center / (double)(total_tosses)) * 4;
    printf("valore di pi greco stimato : %lf\n", esteem);

    srand(time(NULL));
}
