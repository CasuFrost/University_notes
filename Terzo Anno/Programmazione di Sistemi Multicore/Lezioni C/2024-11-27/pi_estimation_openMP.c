
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

static long num_trials = 100000000;

double get_rand_minus_one_one(unsigned int *seed)
{
    return 2 * (rand_r(seed) / (double)RAND_MAX) - 1;
}

int main()
{
    long i;
    long Ncirc = 0;
    double pi, x, y, test, total_time;
    double r = 1.0; // radius of circle. Side of squrare is 2*r
    srand(time(NULL));

    total_time = omp_get_wtime();
#pragma omp parallel
    {
        unsigned int seed = omp_get_thread_num();
#pragma omp single
        printf(" %d threads ", omp_get_num_threads());

#pragma omp for reduction(+ : Ncirc) private(x, y, test)
        for (i = 0; i < num_trials; i++)
        {
            x = get_rand_minus_one_one(&seed);
            y = get_rand_minus_one_one(&seed);

            test = x * x + y * y;

            if (test <= r * r)
                Ncirc++;
        }
    }

    pi = 4.0 * ((double)Ncirc / (double)num_trials);

    printf("\n %ld trials, pi is %f ", num_trials, pi);
    printf(" in %f seconds\n", omp_get_wtime() - total_time);

    return 0;
}