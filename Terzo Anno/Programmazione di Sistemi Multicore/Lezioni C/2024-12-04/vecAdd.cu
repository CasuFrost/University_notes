#include <stdio.h>
#include <cuda.h>

__global__ void vecAddKernel(float *A, float *B, float *C, int n)
{
    int index = blockDim.x * blockIdx.x + threadIdx.x;
    if (index < n)
    {
        C[index] = A[index] + B[index];
    }
}

void vecAdd(float *h_A, float *h_B, float *h_C, int n)
{
    float *d_A, *d_B, *d_C;
    cudaMalloc((void **)&d_A, n * sizeof(float));
    cudaMemcpy(d_A, h_A, n * sizeof(float), cudaMemcpyHostToDevice);
    cudaMalloc((void **)&d_B, n * sizeof(float));
    cudaMemcpy(d_B, h_B, n * sizeof(float), cudaMemcpyHostToDevice);
    cudaMalloc((void **)&d_C, n * sizeof(float));

    vecAddKernel<<<ceil(n / 256.0), 256>>>(d_A, d_B, d_C, n);
    cudaDeviceSynchronize();
    cudaMemcpy(h_C, d_C, n * sizeof(float), cudaMemcpyDeviceToHost);

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
}

#define SIZE 10000

int main()
{
    float a[SIZE];
    float b[SIZE];
    float c[SIZE];
    for (size_t i = 0; i < SIZE; i++)
    {
        a[i] = 1.5;
        b[i] = 0.5;
    }
    vecAdd(a, b, c, SIZE);
}