#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void print_set(sigset_t *set)
{
  for (int i = 1; i < 32; i++)
  {
    if (sigismember(set, i) == 1)
    {
      printf("è presente il segnale %d\n", i);
    }
  }
}

int check(sigset_t *set)
{
  return (sigismember(set, 2) == 1) || (sigismember(set, 20) == 1);
}

int main(void)
{
  sigset_t set, oset, pset;
  printf("%d\n", getpid());
  /*int sigemptyset(sigset_t *set);
  Rimuove tutti i segnali da set
  Significa tutti i segnali sono abilitati e  vengono ricevuti */

  while (1)
  {
    sleep(5);
    printf("waiting signal\n");
    sigpending(&pset);

    if (check(&pset))
    {
      printf("Eliminato da console\n");
      return (EXIT_SUCCESS);
    }
  }

  if (sigemptyset(&set) == -1)
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  }

  /* il contrario e' sigfillset(&set), che mette tutti i segnali nel set */

  /* int sigaddset(sigset_t *set, int signum);
  mette signum nel set, quindi lo maschera (disabilita) */
  if (sigaddset(&set, SIGINT))
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  } /* il contrario e' sigdelset, che toglie un segnale dal set */
  if (sigaddset(&set, SIGUSR1))
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  }

  if (sigprocmask(SIG_BLOCK, &set, &oset) == -1)
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  }

  /* inizio sezione critica */

  if (sigpending(&pset) == -1)
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  } /*restituisce i segnali che sono pending*/
  /* chiamare print_set(&pset) */

  printf("dentro\n");

  kill(getpid(), SIGINT);
  kill(getpid(), SIGUSR1);

  printf("ancora dentro\n");

  if (sigpending(&pset) == -1)
  {
    printf("Errore\n");
    exit(EXIT_FAILURE);
  }
  /* chiamare print_set(&pset) (esercizio 1) */
  /* fine sezione critica */

  print_set(&pset);

  // sigprocmask(SIG_UNBLOCK, &set, &oset);

  printf("fuori\n");

  // kill( getpid(), SIGINT );
  // printf("dopo\n");

  /* termina con un SIGINT */
  return (EXIT_SUCCESS);
}
