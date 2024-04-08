#include <stdio.h>
#include <string.h>
	 
#include <sys/types.h>
#include <unistd.h>
	 
#include <stdlib.h>   // Declaration for exit()
	 
int globalVariable = 2;
	 
int main()
{
  char *sIdentifier;
  int    iStackVariable = 20;
	 
  pid_t pID = fork();
  if (pID == 0)                // child
    {
      // Code only executed by child process
	 
      sIdentifier = "Child Process: ";
      globalVariable++;
      iStackVariable++;
    }
  else if (pID < 0)            // failed to fork
    {
      fprintf(stderr, "Failed to fork\n");
      exit(1);
      // Throw exception
    }
  else                                   // parent
    {
      // Code only executed by parent process
	 
      sIdentifier = "Parent Process:";
    }
	 
  // Code executed by both parent and child.
	   
  printf("%s\n", sIdentifier);
  printf(" Global variable: %d\n", globalVariable);
	  
}
