// Implements counting sort
// First argument from command line is the maximum value that each element in the array can have.
// e.g., if the argument is 100, then each element of the array can contain a value between 0 and 100.
// You can assume that the size of the array is much larger than the maximum value.
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define ARRAY_SIZE 10000000

int main(int argc, char **argv)
{
    int max = 10;
    if (argc > 1)
        max = atoi(argv[1]);
    int *array = (int *)malloc(ARRAY_SIZE * sizeof(int));
    int *counts = (int *)malloc(max * sizeof(int));
    // Generate random array
    for (unsigned long i = 0; i < ARRAY_SIZE; i++)
    {
        array[i] = rand() % max;
    }

    double start = omp_get_wtime();
    for (unsigned long i = 0; i < max; i++)
    {
        counts[i] = 0;
    }

    for (unsigned long i = 0; i < ARRAY_SIZE; i++)
    {
        counts[array[i]]++;
    }
    double stop = omp_get_wtime();

    /*for (unsigned long i = 0; i < max; i++)
    {
        printf("%d elements with value %ld\n", counts[i], i);
    }*/
    printf("Total runtime: %f secs\n", stop - start);

    free(counts);
    free(array);
    return 0;
}