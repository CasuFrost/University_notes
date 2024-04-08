#include <stdio.h>
#include <sys/mman.h>

int main(){

    void *a;
    int fd = 0;
    a=mmap(NULL,50,PROT_READ,MAP_PRIVATE,fd,0);

    // con il metodo msync aggiorna le modifiche su disco, ritorna -1 se c'è un errore
    msync(a,0,0);


    //Quando si finisce di usare l'area di memoria, va de-mappata, ritorna -1 se c'è un errore
    munmap(a,0);
    return 0;
}