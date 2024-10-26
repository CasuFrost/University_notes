#include <stdio.h>
#include <mpi.h>

int main(void)
{

    int rank = 0;
    int size = 0;
    int send_right = 19;
    int send_left = 23;
    int recv_right = 19;
    int recv_left = 23;

    MPI_Init(NULL, NULL);

    MPI_Comm_rank(MPI_COMM_WORLD, rank);
    MPI_Comm_size(MPI_COMM_WORLD, size);

    // Dichiaro le variabili per lo status delle chiamate

    MPI_Request req[4];

    // Invio al destro
    MPI_Isend(&send_right, 1, MPI_INT, (rank + 1) % size, 0, MPI_COMM_WORLD, &req[0]);

    // invio al sinistro
    MPI_Isend(&send_left, 1, MPI_INT, (rank - 1) % size, 0, MPI_COMM_WORLD, &req[1]);

    // Invio al destro
    MPI_Irecv(&recv_right, 1, MPI_INT, (rank + 1) % size, 0, MPI_COMM_WORLD, &req[2]);

    // invio al sinistro
    MPI_Irecv(&recv_left, 1, MPI_INT, (rank - 1) % size, 0, MPI_COMM_WORLD, &req[3]);

    MPI_Waitall(4, req, MPI_STATUS_IGNORE);
    MPI_Finalize();
}