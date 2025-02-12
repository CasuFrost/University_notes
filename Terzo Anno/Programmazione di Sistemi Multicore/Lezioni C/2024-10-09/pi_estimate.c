#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>

int main(int argc, char **argv)
{

    long int precision = 5000000000; // Numero di punti generati casualmente

    if (argc > 1)
    {
        precision = atoi(argv[1]);
    }

    MPI_Init(NULL, NULL);
    srand(time(NULL));

    int my_rank;
    int my_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &my_size);

    long int local_precision = precision / my_size; // Numero di punto da generare per ogni processo
    long int local_circle_point = 0;

    for (int i = 0; i <= local_precision; i++)
    {
        double x = (double)rand() / RAND_MAX * 2.0 - 1.0; // Generazione casuale punto
        double y = (double)rand() / RAND_MAX * 2.0 - 1.0;
        if (x * x + y * y < 1) // Controllo se il punto è nel cerchio
            local_circle_point++;
    }

    long int total_circle_point = 0;
    MPI_Reduce(&local_circle_point, &total_circle_point, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (my_rank == 0)
    {
        double esteem = ((double)total_circle_point / precision * 4);
        printf("Su %ld punti, la stima del pi greco e' : %lf\n", precision, esteem);
    }

    MPI_Finalize();
    return 0;
}