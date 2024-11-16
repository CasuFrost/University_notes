#include <stdio.h>
#include <stdlib.h>
#include <opm.h>

void Trap(double a, double b, int n, double *global_result_p)
{
    double h, x, my_result;
    double local_a, local_b;
    int i, local_n;
#ifdef _OPENMP
    int my_rank = omp_get_thread_num();
    int thread_count = omp_get_num_threads();
#else
    int my_rank = 0;
    int thread_count = 1;
#endif

    h = (b - a) / n;
    local_n = n / thread_count;
    local_a = a + my_rank * local_n * h;
    my_result = (f(local_a) + f(local_b)) / 2.0; /*f è la funzione integranda*/
    for (i = 0; i <= local_n - 1; i++)
    {
        x = local_a + i * h;
        my_result += f(x);
    }
    my_result = my_result * h;
#pragma omp critical
    *global_result_p += my_result;
}

void main(int argc, char **argv)
{
    double global_result = 0.0;
    double a, b;
    int n;
    int thread_count = atoi(argv[1]);
    printf("Enter a,b and n\n", &a, &b, &n);
#pragma omp parallel num_threads(thread_count);
    Trap(a, b, n, &global_result);

    printf("result : %f", global_result);
}