#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>

/* vedere http://www.linuxhowtos.org/C_C++/socket.htm per una descrizione del paradigma
   client-server e delle syscall necessarie a client e server */

/* Per lanciarli: prima ./server, poi ./client localhost 123456 */

/* ESERCIZIO: fare in modo che la porta sia letta come argomento ulteriore tanto dal client
   quanto dal server */

/* ESERCIZIO: far si' che, per ogni accept che va a buon fine, venga creato un processo che
   "serve" la richiesta (mandando l'ora) */

/* ESERCIZIO: implementare una piccola chat testuale sincrona, prima con le fifo, poi con le
   socket. Assumere che ci siano 2 soli utenti, il primo che parla attraverso il server,
   il secondo che parla attraverso il client. Occorre inviare un messaggio solo quando viene
   premuto il tasto invio. Un processo puo' inviare un messaggio solo dopo averne ricevuto un
   altro (tranne che per l'inizio della comunicazione, che viene sempre dato dal client) */

int main(int argc, char *argv[])
{
   if (argc != 2)
   {
      printf("inserire numero di porta\n");
      exit(1);
   }
   int listenfd = 0, connfd = 0;
   struct sockaddr_in serv_addr;

   char sendBuff[1025];
   time_t ticks;

   listenfd = socket(AF_INET, SOCK_STREAM, 0);
   memset(&serv_addr, 0, sizeof(serv_addr));
   memset(sendBuff, 0, sizeof(sendBuff));

   serv_addr.sin_family = AF_INET;
   serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
   serv_addr.sin_port = htons(atoi(argv[1])); /*converte uno short int in formato network
                             utile per numeri di porta*/

   bind(listenfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

   listen(listenfd, 10);

   while (1)
   {
      connfd = accept(listenfd, (struct sockaddr *)NULL, NULL); /* non ci interessa
                    il descrittore del nuovo  socket creato e quindi
                    passiamo NULL come indirizzo e come  dimensione  della
                    struttura dati */

      pid_t pid = fork();

      if (pid == 0)
      {
         ticks = time(NULL);

         snprintf(sendBuff, sizeof(sendBuff), "ciao cazzo %.24s\r\n", ctime(&ticks));

         write(connfd, sendBuff, strlen(sendBuff));

         close(connfd);
         exit(0);
      }
      else
      {
         close(connfd);
      }
   }
}
