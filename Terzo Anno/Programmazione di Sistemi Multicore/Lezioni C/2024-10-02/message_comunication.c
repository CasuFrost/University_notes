#include <stdio.h>
#include <mpi.h>

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
    int str_size = 256;
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == 0)
    {
        printf("hello world, i am process %d of %d. I will recive messages from other cores.\n", rank, size);
        char str[str_size];
        for (int i = 1; i <= size; i++)
        {
            MPI_Recv(str, str_size, MPI_CHAR, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("(STRING RECIVED) : %s", str);
        }
    }
    else
    {
        char str[str_size];
        sprintf(str, "hello world, i am process %d of %d\n", rank, size);
        // Si invia al processo 0
        MPI_Send(str, str_size, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize(); // Serve per terminare la libreria
    return 0;
}