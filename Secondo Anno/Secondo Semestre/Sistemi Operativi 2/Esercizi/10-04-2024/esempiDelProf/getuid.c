#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

#include <pwd.h>

/* ESERCIZIO: fare in modo che venga stampato anche il nome dell'utente */

int main(void)
{
  printf("My userid is %d\n", getuid());

  struct passwd *pws;       // Inizializza la struttura con le informazioni dell'utente
  pws = getpwuid(getuid()); // Ottengo informazioni sull'utente relativo all'id dell'utente
  printf("My user name is %s\n", pws->pw_name);

  return EXIT_SUCCESS;
}