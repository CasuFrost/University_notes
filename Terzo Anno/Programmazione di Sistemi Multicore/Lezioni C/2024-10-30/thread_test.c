#include <stdio.h>
#include <pthread.h>

void print_thread_id(int id)
{
    printf("sono il thread con id : %d\n", id);
}

int main()
{
    pthread_t tid;
    void (*func_ptr)(int) = print_thread_id;
    pthread_create(tid, NULL, *func_ptr, NULL);
}