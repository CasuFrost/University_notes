#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/fcntl.h>
#include <stdlib.h> // Declaration for exit()

int globalVariable = 2;

int main(int argc, char *argv[])
{

    FILE *fp;

    fp = fopen(argv[1], "r+");

    if (argc < 2)
    {
        printf("bisogna fornire un file\n");
        exit(1);
    }

    char *sIdentifier;
    int iStackVariable = 20;

    pid_t pID = fork();
    if (pID == 0) // child
    {
        // Code only executed by child process

        fprintf(fp, "First child Process:\n Global variable: %d\n", globalVariable);
        globalVariable++;
        iStackVariable++;
    }
    else if (pID < 0) // failed to fork
    {
        fprintf(stderr, "Failed to fork\n");
        exit(1);
        // Throw exception
    }
    else // parent
    {
        // Code only executed by parent process
        wait(NULL);

        pid_t pID2 = fork();
        if (pID2 == 0) // child
        {
            iStackVariable++;
            fprintf(fp, "Second child Process:\n Global variable: %d\n", globalVariable);
        }
        else
        {
            wait(NULL);
            fprintf(fp, "Parent Process:\n Global variable: %d\n", globalVariable);
        }
    }
    fclose(fp);
    // Code executed by both parent and child.
    exit(0);
}