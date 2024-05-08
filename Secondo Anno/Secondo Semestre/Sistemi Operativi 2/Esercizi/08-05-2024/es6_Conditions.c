#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int myVar = 0;
pthread_cond_t cond;
struct Test
{
    int a;
    int b;
};

struct Test test;

void start()
{
    for (int i = 0; i < 10; i++)
    {
        test.a++;
        test.b++;
        sleep(1);
        printf("a := %d    b := %d\n", test.a, test.b);
    }
}

int main(int argc, char *argv[])
{
    pthread_cond_init(&cond, NULL);

    pthread_t tid1;
    pthread_t tid2;

    pthread_create(&tid1, 0, start, NULL);
    pthread_create(&tid2, 0, start, NULL);

    pthread_join(tid1, (int *)&argc);
    pthread_join(tid2, (int *)&argc);

    printf("La variabile a assume valore %d e la b assume valore %d\n", test.a, test.b);

    return EXIT_SUCCESS;
}