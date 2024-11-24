/*

PRODOTTO FRA MATRICI QUADRATE

Implementa la moltiplicazione tra matrici in Pthread. Supponiamo di eseguire questo programma su p processi (da 0 a p-1).
Le due matrici di input vengono generate casualmente dal processo di rango p-1. L'ordine delle matrici deve essere letto
da argv (il che significa che puoi usare un array, ma devi allocare memoria dinamicamente). Dopo aver calcolato la matrice risultante,
deve essere memorizzata nella memoria del processo di rango 0.

    - Verifica: Controlla se la matrice risultante è corretta, ad esempio eseguendo lo stesso calcolo in modo sequenziale.
    - Esplora alternative: Prova a pensare a diversi modi per implementare questa operazione.

*/

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX_MATRIX_VALUE 10
#define THREAD_NUM 4

struct t_data
{
    int **mat1;
    int **mat2;
    int **result_mat;
    int rank;
    int row_num;
    int order;
};
void print_matrix_product(int **m1, int **m2, int **m3, int order)
{
    for (int i = 0; i < order; i++)
    {
        for (int j = 0; j < order; j++)
        {
            printf("%d ", (int)m1[i][j]);
        }
        if (i == order / 2)
        {
            printf(" *  ");
        }
        else
        {
            printf("    ");
        }
        for (int j = 0; j < order; j++)
        {
            printf("%d ", (int)m2[i][j]);
        }
        if (i == order / 2)
        {
            printf(" =  ");
        }
        else
        {
            printf("    ");
        }
        for (int j = 0; j < order; j++)
        {
            printf("%d ", (int)m3[i][j]);
        }
        printf("\n");
    }
}
void print_matrix(int **m, int order)
{
    for (int i = 0; i < order; i++)
    {
        for (int j = 0; j < order; j++)
        {
            printf("%d ", (int)m[i][j]);
        }
        printf("\n");
    }
}

void print_matrix_wolfram(int **m, int order)
{
    printf("{");
    for (int i = 0; i < order; i++)
    {
        printf("{");
        for (int j = 0; j < order; j++)
        {
            if (j != order - 1)
                printf("%d,", (int)m[i][j]);
            else
                printf("%d", (int)m[i][j]);
        }
        if (i != order - 1)
            printf("},");
        else
            printf("}");
    }
    printf("}");
}

void mat_random_generation(int **m, int order, int factor)
{
    for (int i = 0; i < order; i++)
    {
        for (int j = 0; j < order; j++)
        {

            m[i][j] = (rand() % MAX_MATRIX_VALUE) * factor;
        }
    }
}

int **create_mat(int order)
{
    int **mat = (int **)malloc(sizeof(int *) * order);
    for (int i = 0; i < order; i++)
    {
        mat[i] = (int *)malloc(sizeof(int) * order);
    }
    return mat;
}

void *thread_func(void *struttura)
{
    // int my_rank = rank;
    struct t_data *data = (struct t_data *)struttura;
    // printf("thread %d. Will operate on rows : %d to %d  \n", data->rank, data->rank * data->row_num, (data->rank + 1) * data->row_num - 1);

    int from_row = data->rank * data->row_num;
    int to_row = (data->rank + 1) * data->row_num - 1;

    // for (int i = from_row; i <= to_row; i++)
    //{
    // printf("%d :\n", data->rank);
    /* ogni i-esima riga di mat 1 con ogni colonna di mat2*/
    for (int k = from_row; k <= to_row; k++)
    {
        for (int i = 0; i < data->order; i++)
        {
            int tmp = 0;
            for (int j = 0; j < data->order; j++)
            {
                tmp += data->mat1[k][j] * data->mat2[j][i];
            }
            data->result_mat[k][i] = tmp;
            // printf("\n");
        }
        // printf("\n");
    }
    // }

    // print_matrix(data->result_mat, data->order);
    fflush(stdout);
    return NULL;
}

int main(int argc, char **argv)
{
    srand(time(NULL));
    int row_per_thread;
    if (argc > 1)
        row_per_thread = atoi(argv[1]);
    else
        row_per_thread = 1;
    int order = row_per_thread * THREAD_NUM; /*matrix order must be divisible by thread number*/
    /*each thread will multiply 'row_per_thread' rows from first matrix, with all the columns of the second matrix */

    /*Random matrix generation*/
    int **mat1 = create_mat(order);
    int **mat2 = create_mat(order);
    int **result_mat = create_mat(order);
    mat_random_generation(result_mat, order, 0);
    mat_random_generation(mat1, order, 1);
    mat_random_generation(mat2, order, 1);
    /*Random matrix generation*/

    pthread_t tids[THREAD_NUM];
    struct t_data tmp;
    tmp.mat1 = mat1;
    tmp.mat2 = mat2;
    tmp.result_mat = result_mat;
    tmp.row_num = row_per_thread;
    tmp.order = order;
    for (int i = -1; i < THREAD_NUM; i++)
    {
        tmp.rank = i;

        pthread_create(&tids[i], NULL, thread_func, (void *)&tmp);
    }
    for (int i = -1; i < THREAD_NUM; i++)
    {
        pthread_join(tids[i], NULL);
    }

    print_matrix_wolfram(mat1, order);
    print_matrix_wolfram(mat2, order);
    printf("=");
    print_matrix_wolfram(result_mat, order);
    fflush(stdout);
    printf("\n");
    print_matrix(mat1, order);
    printf("\n");
    print_matrix(mat2, order);
    printf("\n");
    printf("\n");
    print_matrix(result_mat, order);
    fflush(stdout);
    printf("\n");
    return 0;
}