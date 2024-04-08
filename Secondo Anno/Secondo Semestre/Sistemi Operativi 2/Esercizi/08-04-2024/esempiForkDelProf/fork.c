#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

/* Esempio base di fork */

/* ESERCIZIO: scrivere uno script che, in un ciclo di N iterazioni, con N dato da riga di
   comando, ricompili questo codice cambiando ogni volta il valore di NUM ad un numero
   random tra 1 e 100, e scriva in stdout quanti context switch ci sono stati tra
   padre e figlio. Lo script deve fare in modo da non mostrare l'output del programma
   su stdout */

#define NUM 10

int main(int argc, char **argv)
{
    printf("--beginning of program\n");

    int counter = 0;
    pid_t pid = fork();

    /* da qui in poi ci sono 2 processi (a meno che pid == -1, ovvero che la fork sia fallita)
       che eseguono questo identico codice. Grazie al fatto che nei 2 processi la variabile
       pid ha valori diversi, si puo' far si' che i 2 processi effettuino operazioni
       diverse (usualmente, collaborando l'uno con l'altro, anche se in questo esempio
       semplice non e' cosi')*/
    
    if (pid == 0)
    {
        // child process
        int i = 0;
        for (; i < NUM; ++i)
        {
	  /* i dati dei 2 processi sono replicati in zone diverse della RAM, e partono
	     (subito dopo la fork) da valori identici. Dalla fork in poi, qualsiasi
	     modifica fatta da uno dei 2 processi ad una di queste variabili resta locale
	     al processo che la fa. Quindi, il primo di questi ++counter ha l'effetto di
	     cambiare counter da 0 ad 1 solo sul figlio e non sul padre. */
	  printf("child process PID %d: counter=%d\n", getpid(), ++counter);
        }
	printf("--end of child program--\n");
	exit(1);
    }
    else if (pid > 0)
    {
        // parent process
        int j = 0;
        for (; j < NUM; ++j)
        {
	  printf("parent process PID %d: counter=%d\n", getpid(), ++counter);
        }
    }
    else
    {
        // fork failed
        printf("fork() failed!\n");
        return 1;
    }

    printf("--end of parent program--\n");

    printf("Try to give the following command: ps -opid,s,cmd %d (you have 60 seconds)\n", pid);
    sleep(60);
        
    return 0;
}
