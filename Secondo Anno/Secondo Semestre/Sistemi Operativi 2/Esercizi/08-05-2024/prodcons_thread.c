#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>
#include <time.h>
#define cbuf_size 33
#define WRITE_FREQUENCY 4
struct circular_buffer
{
    pthread_mutex_t mtx;
    int S; /* Start */
    int E; /* End */
    char buf[cbuf_size];
    pthread_t writer[cbuf_size];
};

struct circular_buffer cb;

void *consume(void *p)
{
    struct circular_buffer *cb = p;
    char str[50];
    for (;;)
    {
        if (pthread_mutex_lock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_lock");
            exit(EXIT_FAILURE);
        }
        while (cb->S == cb->E)
        {
            /* circular buffer empty */;
            if (pthread_mutex_unlock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_unlock");
                exit(EXIT_FAILURE);
            }
            usleep(100000);
            if (pthread_mutex_lock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_lock");
                exit(EXIT_FAILURE);
            }
        }
        //        putchar(cb->buf[cb->S]); /*Versione originale esempio */

        sprintf(str, " Consumatore \"%08x\" ha letto \'%c\' prodotta da \"%08x\"", pthread_self(), cb->buf[cb->S], cb->writer[cb->S]);
        /* versione Esercizio da esempio */
        puts(str);
        fflush(stdout);
        cb->S = (cb->S + 1) % cbuf_size;
        if (pthread_mutex_unlock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_unlock");
            exit(EXIT_FAILURE);
        }
        usleep(100000);
    }
}

void *produce(void *p)
{
    struct circular_buffer *cb = p;
    for (;;)
    {
        int c, nE;
        c = getchar();
        if (c == EOF)
            break;
        if (pthread_mutex_lock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_lock");
            exit(EXIT_FAILURE);
        }
        nE = (cb->E + 1) % cbuf_size;
        /* controllare se buffer pieno */
        while (nE == cb->S)
        {
            /* buffer pieno */
            if (pthread_mutex_unlock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_unlock");
                exit(EXIT_FAILURE);
            }
            usleep(100000);
            if (pthread_mutex_lock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_lock");
                exit(EXIT_FAILURE);
            }
            nE = (cb->E + 1) % cbuf_size;
        }
        cb->writer[cb->E] = pthread_self();
        cb->buf[cb->E] = c;
        cb->E = nE;
        if (pthread_mutex_unlock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_unlock");
            exit(EXIT_FAILURE);
        }
    }
    return NULL;
}

void *produceRandom(void *p)
{
    struct circular_buffer *cb = p;
    for (;;)
    {
        int nE;
        // c = getchar();
        if (pthread_mutex_lock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_lock");
            exit(EXIT_FAILURE);
        }
        nE = (cb->E + 1) % cbuf_size;
        /* controllare se buffer pieno */
        while (nE == cb->S)
        {
            /* buffer pieno */
            if (pthread_mutex_unlock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_unlock");
                exit(EXIT_FAILURE);
            }
            usleep(100000);
            if (pthread_mutex_lock(&cb->mtx) != 0)
            {
                perror("pthread_mutex_lock");
                exit(EXIT_FAILURE);
            }
            nE = (cb->E + 1) % cbuf_size;
        }
        int c = 65 + (rand() % 57);

        cb->writer[cb->E] = pthread_self();
        cb->buf[cb->E] = c;
        cb->E = nE;
        if (pthread_mutex_unlock(&cb->mtx) != 0)
        {
            perror("pthread_mutex_unlock");
            exit(EXIT_FAILURE);
        }
        sleep(WRITE_FREQUENCY);
    }
    return NULL;
}

int main(void)
{
    srand(time(NULL));
    int s;
    pthread_t t;

    cb.E = cb.S = 0;
    if (pthread_mutex_init(&cb.mtx, NULL) != 0)
    {
        fprintf(stderr, "Error in pthread_mutex_init()\n");
        exit(EXIT_FAILURE);
    }

    s = pthread_create(&t, NULL, consume, &cb);
    if (s != 0)
    {
        fprintf(stderr, "Error in pthread_create()\n");
        exit(EXIT_FAILURE);
    }

    s = pthread_create(&t, NULL, consume, &cb);
    if (s != 0)
    {
        fprintf(stderr, "Error in pthread_create()\n");
        exit(EXIT_FAILURE);
    }

    s = pthread_create(&t, NULL, produceRandom, &cb);
    if (s != 0)
    {
        fprintf(stderr, "Error in pthread_create()\n");
        exit(EXIT_FAILURE);
    }
    produce(&cb);

    return 0; /* NEVER REACHED */
}