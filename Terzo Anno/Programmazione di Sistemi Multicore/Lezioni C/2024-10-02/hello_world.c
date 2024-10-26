#include <stdio.h>
#include <mpi.h>
// voglio lanciare il programma su più unita di calcolo
int main(int argc, char **argv)
{
    int p = MPI_Init(NULL, NULL);
    // Il parametro in output di MPI_Init è uno status sull'errore
    if (p != MPI_SUCCESS)
    {
        printf("qualcosa è andato storto");
        MPI_Abort(MPI_COMM_WORLD, p);
        // Con MPI_Abort tutti i processi su tutti i core avviati verranno terminati
    }
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    printf("hello world, i am process %d of %d\n", rank, size);
    MPI_Finalize(); // Serve per terminare la libreria
    return 0;
}