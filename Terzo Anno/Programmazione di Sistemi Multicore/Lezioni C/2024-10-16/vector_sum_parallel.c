#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

void print_vector(int n, int *v, char name)
{
    printf("%c = [ ", name);
    for (int i = 0; i < n - 1; i++)
    {
        printf("%d, ", v[i]);
    }
    printf("%d ]\n", v[n - 1]);
}

int main(int argc, char **argv)
{
    MPI_Init(NULL, NULL);

    int my_rank;
    int size;
    int local_size = 3;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_vector[size];
    int local_vector2[size];
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

    if (my_rank == 0)
    {

        int inputVector[local_size * size];
        int inputVector2[local_size * size];
        srand(time(NULL));
        for (int i = 0; i < local_size * size; i++)
        {
            inputVector[i] = rand() % 100;
            inputVector2[i] = rand() % 100;
        }
        print_vector(local_size * size, inputVector, 'A');
        print_vector(local_size * size, inputVector2, 'B');
        printf("\n");
        MPI_Scatter(inputVector, local_size, MPI_INT, local_vector, local_size, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Scatter(inputVector2, local_size, MPI_INT, local_vector2, local_size, MPI_INT, 0, MPI_COMM_WORLD);
    }
    else
    {
        MPI_Scatter(NULL, local_size, MPI_INT, local_vector, local_size, MPI_INT, 0, MPI_COMM_WORLD);
        MPI_Scatter(NULL, local_size, MPI_INT, local_vector2, local_size, MPI_INT, 0, MPI_COMM_WORLD);
    }
    printf("process %d :\n     A_%d = [ ", my_rank, my_rank);
    for (int i = 0; i < local_size - 1; i++)
    {
        printf("%d, ", local_vector[i]);
    }
    printf("%d ]\n     B_%d = [", local_vector[local_size - 1], my_rank);
    for (int i = 0; i < local_size - 1; i++)
    {
        printf("%d, ", local_vector2[i]);
    }
    printf("%d ]\n A_%d+B_%d = [", local_vector2[local_size - 1], my_rank, my_rank);
    for (int i = 0; i < local_size - 1; i++)
    {
        printf("%d, ", local_vector2[i] + local_vector[i]);
    }
    printf("%d ]\n\n", local_vector2[local_size - 1] + local_vector[local_size - 1]);

    int vec_sum[local_size];
    for (int i = 0; i < local_size; i++)
    {
        vec_sum[i] = local_vector2[i] + local_vector[i];
    }

    if (my_rank == 0)
    {
        int outVector[local_size * size];
        MPI_Gather(vec_sum, local_size, MPI_INT, outVector, local_size, MPI_INT, 0, MPI_COMM_WORLD);
        print_vector(local_size * size, outVector, 'O');
    }
    else
    {
        MPI_Gather(vec_sum, local_size, MPI_INT, NULL, local_size, MPI_INT, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();

    exit(0);
}