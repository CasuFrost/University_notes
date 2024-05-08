#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

pthread_mutex_t mtx;
int myVar = 0;

struct Test
{
    int a;
    int b;
};

struct Test test;

void start(char name[40])
{
    for (int i = 0; i < 10; i++)
    {
        if (pthread_mutex_lock(&mtx) != 0)
        {
            perror("pthread_mutex_lock");
            exit(EXIT_FAILURE);
        }
        test.a++;
        test.b++;

        printf("%s modifica le variabili : \n   a := %d    b := %d\n--------------\n", name, test.a, test.b);
        if (pthread_mutex_unlock(&mtx) != 0)
        {
            perror("pthread_mutex_unlock");
            exit(EXIT_FAILURE);
        }
        sleep(1);
    }
}

int main(int argc, char *argv[])
{
    if (pthread_mutex_init(&mtx, NULL) != 0)
    {
        fprintf(stderr, "Error in pthread_mutex_init()\n");
        exit(EXIT_FAILURE);
    }
    pthread_t tid1;
    pthread_t tid2;
    char name[40] = "thread1";
    char name2[40] = "thread2";
    pthread_create(&tid1, 0, start, name);
    pthread_create(&tid2, 0, start, name2);

    pthread_join(tid1, (int *)&argc);
    pthread_join(tid2, (int *)&argc);

    printf("La variabile a assume valore %d e la b assume valore %d\n", test.a, test.b);

    return EXIT_SUCCESS;
}