#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

long start(long v) {
    return v+1;
}

int main(int argc, char *argv[]) {

    pthread_t tid;

    /* man 3 - pthread e' comunque una libreria del kernel

    int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                          void *(*start_routine) (void *), void *arg); */

    /* Per compilare: gcc pthreadHW.c -pthread */

    /* creo un thread per eseguire la funzione start() di cui sopra */
    pthread_create(&tid, 0, (long *) start, (long) argc);

    /* attendo la terminazione del thread e ricevo il valore di ritorno */
    pthread_join(tid, (int *) &argc);

    printf("returning %ld\n", argc);
    return EXIT_SUCCESS;
}


