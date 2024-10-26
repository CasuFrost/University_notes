/*

PRODOTTO FRA MATRICI QUADRATE

Implementa la moltiplicazione tra matrici in MPI. Supponiamo di eseguire questo programma su p processi (da 0 a p-1).
Le due matrici di input vengono generate casualmente dal processo di rango p-1. L'ordine delle matrici deve essere letto
da argv (il che significa che puoi usare un array, ma devi allocare memoria dinamicamente). Dopo aver calcolato la matrice risultante,
deve essere memorizzata nella memoria del processo di rango 0.

    - Verifica: Controlla se la matrice risultante è corretta, ad esempio eseguendo lo stesso calcolo in modo sequenziale.
    - Esplora alternative: Prova a pensare a diversi modi per implementare questa operazione.

*/

#include <mpi.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

void print_matrix(int *mat, int mat_size, int column_size)
{
    int check = 0;
    printf("\n");
    for (int i = 0; i < mat_size; i++)
    {
        if (!check)
        {
            check = 1;
            printf("|  ");
        }
        if (mat[i] < 10)
            printf("%d   ", mat[i]);
        else
            printf("%d  ", mat[i]);
        if ((i + 1) % column_size == 0)
        {
            printf("|\n");
            check = 0;
        }
    }
    printf("\n");
}

int main(int argc, char **argv)
{
    MPI_Init(NULL, NULL);

    /*ottenimento di rank e numero di processi distinti*/
    int rank, comm_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &comm_size);

    /*definizione dell'ordine della matrice*/
    int matrix_order; /*ordine della matrice*/
    if (argc == 1)
    {
        matrix_order = comm_size;
    }
    else
    {
        matrix_order = atoi(argv[1]) * comm_size;
    }

    int matrix_size = matrix_order * matrix_order; /*numero di elementi nella matrice*/
    int *mat1 = malloc(sizeof(int) * matrix_size);
    int *mat2 = malloc(sizeof(int) * matrix_size);
    int *output_mat = malloc(sizeof(int) * matrix_size);
    for (int i = 0; i < matrix_size; i++)
    {
        output_mat[i] = 0;
    }

    /*il processo di rank comm_size-1 genera la matrice di ordine divisibile per il numero dei rank*/
    if (rank == comm_size - 1)
    {
        printf("verrà generata una matrice %dx%d di numeri interi casuali compresi fra 0 e 100\n", comm_size, comm_size);

        srand(time(NULL)); /*per i numeri casuali*/

        for (int i = 0; i < matrix_size; i++)
        {
            mat1[i] = rand() % 100;
            mat2[i] = rand() % 100;
        }

        printf("verrà eseguito il prodotto delle due matrici :\n\n");
        print_matrix(mat1, matrix_size, matrix_order);
        print_matrix(mat2, matrix_size, matrix_order);

        MPI_Bcast(mat1, matrix_size, MPI_INT, comm_size - 1, MPI_COMM_WORLD);
        MPI_Bcast(mat2, matrix_size, MPI_INT, comm_size - 1, MPI_COMM_WORLD);
    }
    else
    {
        MPI_Bcast(mat1, matrix_size, MPI_INT, comm_size - 1, MPI_COMM_WORLD);
        MPI_Bcast(mat2, matrix_size, MPI_INT, comm_size - 1, MPI_COMM_WORLD);
    }

    /*a questo punto, ogni processo ha le due matrici e deve occuparsi di fare il prodotto*/
    int local_row_number = matrix_order / comm_size;

    /*Ogni processo dovrà occuparsi di (matrix_order*local_row_number) elementi */

    /*il processo p si occupa delle righe comprese fra gli elementi    [p*(matrix_order*local_row_number)],   [p* +(matrix_order*local_row_number) - 1] */

    /*il processo p si occupa delle righe
        p*local_row_number
        p*local_row_number  + local_row_number - 1
        .
        .
        .
    */
    MPI_Barrier(MPI_COMM_WORLD);

    for (int i = rank * local_row_number; i < rank * local_row_number + local_row_number; i++)
    {
        /*i è l'indice della riga*/

        /*Riga analizzata dal processo*/
        for (int j = 0; j < matrix_order; j++)
        {

            for (int k = 0; k < matrix_order; k++)
            {
                int sum = 0;
                for (int l = 0; l < matrix_order; l++)
                {
                    sum += mat1[l * matrix_order + k] * mat2[i * matrix_order + j];
                }
                output_mat[i * matrix_order + k] = sum;
            }
        }
    }

    if (rank == 0)
    {
        int *output = malloc(sizeof(int) * matrix_size);
        MPI_Reduce(output_mat, output, matrix_size, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
        printf("matrice risultato : \n");
        print_matrix(output, matrix_size, matrix_order);
    }
    else
    {
        MPI_Reduce(output_mat, NULL, matrix_size, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    }
    MPI_Finalize();
}