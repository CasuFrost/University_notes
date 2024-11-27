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
#include <omp.h>

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

void thread_func(int **mat1, int **mat2, int **result_mat, int order, int row_num)
{

    // int my_rank = rank;
    // printf("thread %d. Will operate on rows : %d to %d  \n", data->rank, data->rank * data->row_num, (data->rank + 1) * data->row_num - 1);
    int rank = omp_get_thread_num();
    int from_row = rank * row_num;
    int to_row = (rank + 1) * row_num - 1;

    // for (int i = from_row; i <= to_row; i++)
    //{
    // printf("%d :\n", rank);
    /* ogni i-esima riga di mat 1 con ogni colonna di mat2*/
    for (int k = from_row; k <= to_row; k++)
    {
        for (int i = 0; i < order; i++)
        {
            int tmp = 0;
            for (int j = 0; j < order; j++)
            {
                tmp += mat1[k][j] * mat2[j][i];
            }
            result_mat[k][i] = tmp;
            // printf("\n");
        }
        // printf("\n");
    }
    // }
    // print_matrix(data->result_mat, data->order);
    return;
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

#pragma omp parallel num_threads(THREAD_NUM)
    thread_func(mat1, mat2, result_mat, order, row_per_thread);
    return 0;
    print_matrix_product(mat1, mat2, result_mat, order);
    printf("\n");
    return 0;
    print_matrix_wolfram(mat1, order);
    print_matrix_wolfram(mat2, order);
    printf("=");
    print_matrix_wolfram(result_mat, order);
    return 0;
}