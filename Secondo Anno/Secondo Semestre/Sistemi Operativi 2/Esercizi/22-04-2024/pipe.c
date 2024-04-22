/*****************************************************************************
 Excerpt from "Linux Programmer's Guide - Chapter 6"
 (C)opyright 1994-1995, Scott Burkett
 *****************************************************************************
 MODULE: pipe.c
*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>

#define _GNU_SOURCE

/* Tipico uso delle pipe: per la comunicazione tra padre e figlio */
double randfrom(double min, double max)
{
  double range = (max - min);
  double div = RAND_MAX / range;
  return min + (rand() / div);
}

void es0()
{
  int fd[2], nbytes;
  pid_t childpid;
  char string[] = "Hello, world!\n";
  char readbuffer[80];

  pipe(fd);

  if ((childpid = fork()) == -1)
  {
    perror("fork");
    exit(1);
  }

  if (childpid != 0)
  {
    /* Child process closes up input side of pipe */
    close(fd[0]);

    /* Send "string" through the output side of pipe */
    printf("Child: Sending: %s\n", string);
    write(fd[1], string, (strlen(string) + 1));
    exit(0);
  }
  else
  {
    /* Parent process closes up output side of pipe */
    close(fd[1]);

    printf("Parent: Receiving\n");
    /* Read in a string from the pipe */
    /* qualora lo scheduler mandasse in esecuzione il padre con la read prima che la write
 del figlio sia completa, il padre si bloccherebbe fino a che il figlio non fa la
 write */
    /* se non si e' attenti a mettere una write in corrispondenza di ogni read, si corre
 il rischio di bloccare indefinitamente un processo */
    nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
    printf("Parent: Received string: %s", readbuffer);
  }

  // return (0);
}

/* ESERCIZIO-1: mostrare che e' possibile invertire i ruoli
 * (il figlio legge e il padre scrive)
 * */

void es1()
{
  int fd[2], nbytes;
  pid_t childpid;
  char string[] = "Hello, world!\n";
  char readbuffer[80];

  pipe(fd);

  if ((childpid = fork()) == -1)
  {
    perror("fork");
    exit(1);
  }

  if (childpid == 0)
  {
    /* Parent process closes up input side of pipe */
    close(fd[0]);

    /* Send "string" through the output side of pipe */
    printf("Parent : Sending: %s\n", string);
    write(fd[1], string, (strlen(string) + 1));
    exit(0);
  }
  else
  {
    /* Child process closes up output side of pipe */
    close(fd[1]);

    printf("Child: Receiving\n");
    /* Read in a string from the pipe */
    /* qualora lo scheduler mandasse in esecuzione il padre con la read prima che la write
 del figlio sia completa, il padre si bloccherebbe fino a che il figlio non fa la
 write */
    /* se non si e' attenti a mettere una write in corrispondenza di ogni read, si corre
 il rischio di bloccare indefinitamente un processo */
    nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
    printf("Child: Received string: %s", readbuffer);
  }
}

/* ESERCIZIO-2: verificare cosa succede se la pipe
 * viene aperta in modalita' non bloccante
 * */

void es2()
{
  int fd[2], nbytes;
  pid_t childpid;
  char string[] = "Hello, world!\n";
  char readbuffer[80];

  pipe2(fd, O_NONBLOCK);

  if ((childpid = fork()) == -1)
  {
    perror("fork");
    exit(1);
  }

  if (childpid == 0)
  {
    /* Parent process closes up input side of pipe */
    close(fd[0]);

    /* Send "string" through the output side of pipe */
    printf("Parent : Sending: %s\n", string);
    write(fd[1], string, (strlen(string) + 1));
    exit(0);
  }
  else
  {
    /* Child process closes up output side of pipe */
    close(fd[1]);

    printf("Child: Receiving\n");
    /* Read in a string from the pipe */
    /* qualora lo scheduler mandasse in esecuzione il padre con la read prima che la write
 del figlio sia completa, il padre si bloccherebbe fino a che il figlio non fa la
 write */
    /* se non si e' attenti a mettere una write in corrispondenza di ogni read, si corre
 il rischio di bloccare indefinitamente un processo */
    nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
    printf("Child: Received string: %s\n", readbuffer);
  }
}

/* ESERCIZIO-3: aggiungere i controlli mancanti sugli errori delle syscall */

/* ESERCIZIO-4: modificare questo programma in modo che legga un intero da riga di comando, il padre lo scriva sulla pipe, e il figlio stampi su stdout quanto letto dalla pipe aumentato di 1; stare attenti a non creare zombie */

void es4(int n)
{
  int fd[2], nbytes;
  pid_t childpid;
  char string[] = "Hello, world!\n";
  char readbuffer[80];

  pipe(fd);

  if ((childpid = fork()) == -1)
  {
    perror("fork");
    exit(1);
  }

  if (childpid == 0)
  {
    /* Parent process closes up input side of pipe */
    close(fd[0]);

    /* Send "string" through the output side of pipe */
    char str[25];
    sprintf(str, "%d", n);

    printf("Parent : Sending: %d\n", n);
    write(fd[1], str, (strlen(str) + 1));
    exit(0);
  }
  else
  {
    /* Child process closes up output side of pipe */
    close(fd[1]);

    printf("Child: Receiving\n");
    /* Read in a string from the pipe */
    /* qualora lo scheduler mandasse in esecuzione il padre con la read prima che la write
 del figlio sia completa, il padre si bloccherebbe fino a che il figlio non fa la
 write */
    /* se non si e' attenti a mettere una write in corrispondenza di ogni read, si corre
 il rischio di bloccare indefinitamente un processo */

    nbytes = read(fd[0], readbuffer, sizeof(readbuffer));
    printf("Child: Received string: %d\n", atoi(readbuffer) + 1);
  }
}

/* ESERCIZIO-5: scrivere un programma in cui il padre manda continuamente un intero ed
   un double al figlio, che gli risponde con la somma (come double, ovviamente). Ad ogni
   ricezione della somma, il padre scrive tale risultato su stdout. Se la somma
   risulta essere zero, il figlio, anziche' mandare la somma sulla pipe, deve mandare
   SIGCHLD al padre e terminare con exit status pari ad n, se n e' il numero delle somme
   calcolate; il padre deve scrivere n prima di terminare a sua volta. */

void es5()
{
  int fd[2];
  int fd2[2];
  pid_t childpid;
  char string[] = "Hello, world!\n";
  char readbuffer[80];

  pipe(fd);
  pipe(fd2);

  if ((childpid = fork()) == -1)
  {
    perror("fork");
    exit(1);
  }

  if (childpid == 0) /* Parent process */
  {

    while (1)
    {

      int rInt = rand() % 100;
      double rDouble = randfrom(-10, 10);
      char str[25];
      sprintf(str, "%d : %f", rInt, rDouble);
      printf("il padre invia %d e %f\n", rInt, rDouble);

      write(fd[1], str, (strlen(str) + 1));

      read(fd2[0], readbuffer, sizeof(readbuffer));
      double d = atof(readbuffer);
      printf("il padre ha ricevuto la somma : %f\n--------------------------\n\n", d);
      sleep(2);
    }
  }
  else
  {

    while (1)
    {
      read(fd[0], readbuffer, sizeof(readbuffer));

      int n;
      double d;
      int j = 0;
      char tmp[40];

      for (int i = 0; i < 50; i++)
      {
        if (readbuffer[i] == ':')
        {
          tmp[j] = '\0';
          n = atoi(tmp);
          j = 0;
          continue;
        }
        tmp[j] = readbuffer[i];
        j++;
      }
      tmp[j] = '\0';
      d = atof(tmp);

      double toSend = (double)n + d;

      char str[25];

      printf("il figlio riceve : %s e crea ed invia la somma %f\n", readbuffer, toSend);

      sprintf(str, "%f", toSend);
      write(fd2[1], str, (strlen(str) + 1));
    }
  }
}

int main(char argc, char *argv[])
{
  srand(time(NULL)); // Initialization, should only be called once.
  if (argc > 1)
  {
    // es4(atoi(argv[1]));
  }
  es5();
  return (0);
}