/* si esegue il prodotto di una matrice 4x4 con un vettore di 4 elementi */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define MAT_ORDER 3
#define THREAD_COUNT 3

/*Variabili globali condivise fra i thread*/
const mat_order = MAT_ORDER;
int x[MAT_ORDER];
int A[MAT_ORDER][MAT_ORDER];
int y[MAT_ORDER];

void print_matrix()
{
    printf("A=\n");
    for (int i = 0; i < mat_order; i++)
    {
        for (int j = 0; j < mat_order; j++)
        {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    printf("\nx=\n");
    for (int j = 0; j < mat_order; j++)
    {
        printf("%d ", x[j]);
    }
    printf("\ny=\n");
    for (int j = 0; j < mat_order; j++)
    {
        printf("%d ", y[j]);
    }
}

void *mat_vec_product(void *rank)
{
    int my_rank = rank;
    int local_m = mat_order / THREAD_COUNT;
    int first_row = my_rank * local_m;
    int last_row = ((my_rank + 1) * local_m) - 1;

    for (int i = first_row; i <= last_row; i++)
    {
        y[i] = 0;

        for (int j = 0; j < mat_order; j++)
        {
            y[i] += A[i][j] * x[j];
        }
    }
    fflush(stdout);
}

int main()
{
    srand(time(NULL));

    /*generazione numeri casuali da 0 a 10*/
    for (int i = 0; i < mat_order; i++)
    {
        x[i] = rand() % 10;
    }
    for (int i = 0; i < mat_order; i++)
    {
        for (int j = 0; j < mat_order; j++)
        {
            A[i][j] = rand() % 10;
        }
    }

    /*creazione dei thread*/
    pthread_t handler[THREAD_COUNT];
    for (int i = 0; i < THREAD_COUNT; i++)
    {
        pthread_create(&handler[i], NULL, mat_vec_product, (void *)i);
    }

    for (int i = 0; i < THREAD_COUNT; i++)
    {
        pthread_join(handler[i], NULL);
    }

    print_matrix();

    return 0;
}