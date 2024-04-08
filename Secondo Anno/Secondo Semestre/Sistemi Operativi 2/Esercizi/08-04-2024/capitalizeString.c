#include <stdio.h>
#include "esempioDelProf/apue.h"
#include <fcntl.h>
#include <sys/mman.h>

#define MAXLEN 100 //caratteri massimi di ogni riga

// Questo programma deve utilizzare MMAP

int main(int argc, char *argv[]){

    if(argc!=2){
        printf("Inserimento parametri errato, va dichiarato un file di testo in input.\n");
        exit(1);
    }

    char* inputFile = argv[1]; //il file in input

    int fdin;
    int fdout;
    struct stat staBuffer;

    if ((fdin = open(argv[1], O_RDONLY)) < 0) {
        printf("errore apertura file.\n");
        exit(1);
    }

    if ((fdout = open("output.txt", O_RDWR | O_CREAT | O_TRUNC, FILE_MODE)) < 0) {
        printf("errore creazione file output.\n");
        exit(1);
    }

    if (fstat(fdin, &staBuffer) < 0) {     // leggo le statistiche del file in input, necessito la dimensione
        printf("fstat error");
        exit(1);
    }

    if (ftruncate(fdout, staBuffer.st_size) < 0) { // il file in output avrà le stesse dimensioni del file in input
        printf("ftruncate error");
        exit(1);
    }

    char *src, *dst;

    src = mmap(0, staBuffer.st_size, PROT_READ, MAP_SHARED, fdin, 0);

    dst = mmap(0, staBuffer.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, fdout, 0);

    memcpy(dst, src,  staBuffer.st_size);

    for(int i=0;i<staBuffer.st_size;i++){ //inverti capitalizzazione
        int c = (int)dst[i];
        if(c>64&&c<91){//c è MAIUSCOLO
            c+=32;
        }   
        else if (c>96&&c<123){ //c è minuscolo
            c-=32;
        }
        dst[i]=(char)c;
    }

       /* does the file copy */
    msync(dst,staBuffer.st_size,0);
    munmap(src,  staBuffer.st_size);
    munmap(dst,  staBuffer.st_size);


    return 0;
}