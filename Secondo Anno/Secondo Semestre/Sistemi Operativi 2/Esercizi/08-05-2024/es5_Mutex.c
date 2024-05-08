#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int myVar = 0;

pthread_mutex_t mtx;

void incrementa(int i, char name[100])
{
    if (pthread_mutex_lock(&mtx) != 0)
    {
        perror("pthread_mutex_lock");
        exit(EXIT_FAILURE);
    }

    int add = (i + 1) * 5;
    printf("%s incrementa di %d, adesso la variabile vale %d\n", name, add, myVar + add);
    myVar += add;
    if (pthread_mutex_unlock(&mtx) != 0)
    {
        perror("pthread_mutex_unlock");
        exit(EXIT_FAILURE);
    }
}

void start(char name[100])
{
    for (int i = 0; i < 10; i++)
    {
        incrementa(i, name);
    }
}

int main(int argc, char *argv[])
{

    if (pthread_mutex_init(&mtx, NULL) != 0)
    {
        fprintf(stderr, "Error in pthread_mutex_init()\n");
        exit(EXIT_FAILURE);
    }
    pthread_t tid;
    char name1[100] = "trhead";
    pthread_create(&tid, 0, start, name1);
    char name2[100] = "main";
    for (int i = 0; i < 10; i++)
    {
        incrementa(i, name2);
    }

    pthread_join(tid, (int *)&argc);

    printf("La variabile assume valore %d\n", myVar);

    return EXIT_SUCCESS;
}