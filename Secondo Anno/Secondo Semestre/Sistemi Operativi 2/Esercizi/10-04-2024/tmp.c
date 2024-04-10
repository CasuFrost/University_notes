#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{

    pid_t pid = fork();

    if (pid == 0)
    {
        // child

        /*Il processo figlio eredita quasi tutto dal processo padre, il codice, la memoria condivisa. Ovviamente
        non eredita il PID*/

        /* Le funzioni 'exec' è possibile caricare un nuovo eseguibile nel processo appena creato, molto utile!*/

        execve("./Scrivania/University_notes/Secondo Anno/Secondo Semestre/Sistemi Operativi 2/Esercizi/10-04-2024/child.out",
               NULL, NULL);
    }
    else
    {
        // parent
        printf("sono il padre\n");

        /* La chiamata wait blocca l'esecuzione del processo padre/chiamante finché non avviene
        un cambiamento di stato in un processo figlio, ritorna informazioni sullo stato del
        processo figlio quando termina. */

        int s;
        wait(&s);

        /*La variabile 's' conterrà il codice di stato del processo figlio terminato*/

        /*La chiamata waitpid è più generale, generalmente attende un qualsiasi figlio che
        termina, ma tale comportamento può essere cambiato con il valore intero
        'options'. */
    }

    exit(0);
}