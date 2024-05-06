
/* EXAMPLE
       The  program below demonstrates the use of pthread_create(), as well as a number of other functions in the pthreads API.

       In the following run, on a system providing the NPTL  threading  implementation,  the  stack  size  defaults to the value given by the "stack size" resource limit:

           $ ulimit -s
           8192            # The stack size limit is 8 MB (0x800000 bytes)
           $ ./a.out hola salut servus
           Thread 1: top of stack near 0xb7dd03b8; argv_string=hola
           Thread 2: top of stack near 0xb75cf3b8; argv_string=salut
           Thread 3: top of stack near 0xb6dce3b8; argv_string=servus
           Joined with thread 1; returned value was HOLA
           Joined with thread 2; returned value was SALUT
           Joined with thread 3; returned value was SERVUS

       In the next run, the program explicitly sets a stack size of 1MB (using
       pthread_attr_setstacksize(3)) for the created threads:

           $ ./a.out -s 0x100000 hola salut servus
           Thread 1: top of stack near 0xb7d723b8; argv_string=hola
           Thread 2: top of stack near 0xb7c713b8; argv_string=salut
           Thread 3: top of stack near 0xb7b703b8; argv_string=servus
           Joined with thread 1; returned value was HOLA
           Joined with thread 2; returned value was SALUT
           Joined with thread 3; returned value was SERVUS
*/
#include <pthread.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <ctype.h>

/*Qui viengono utilizzate le macro per definire delle funzioni.
Quando queste funzioni vengono invocate viene rimpiazzata la chiamatta con il codice della macro - molto piu' efficiente  che chiamare una funzione*/

#define handle_error_en(en, msg) \
    do                           \
    {                            \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)

#define handle_error(msg)   \
    do                      \
    {                       \
        perror(msg);        \
        exit(EXIT_FAILURE); \
    } while (0)

struct thread_info
{                        /* Used as argument to thread_start() */
    pthread_t thread_id; /* ID returned by pthread_create() */
    int thread_num;      /* Application-defined thread # */
    char *argv_string;   /* From command-line argument */
};

/* Thread start function: display address near top of our stack,
   and return upper-cased copy of argv_string */

static void *thread_start(void *arg)
{
    struct thread_info *tinfo = arg;
    char *uargv, *p;

    /* Quando viene creato il thread e quindi eseguita  questa
     funzione le variabili sopra dichiarate vengono
     messe nello stack.
     Il puntatore  *p sara' l'ultima e quindi il
     suo indirizzo di memoria ci da un indicazione di dove si
     trova il top dello stack
     */
    printf("Thread %d: top of stack near %p; argv_string=%s\n",
           tinfo->thread_num, &p, tinfo->argv_string);

    uargv = strdup(tinfo->argv_string); /*funzione che ritorna il  puntatore ad una stringa che e il duplicato dell'argomento*/
    if (uargv == NULL)
        handle_error("strdup"); /*qui usiamo una delle macro sopra definite*/

    for (p = uargv; *p != '\0'; p++)
        *p = toupper(*p); /*Converto ogni carattere della stringa in lettera maiuscola*/

    return uargv;
}

int main(int argc, char *argv[])
{
    int s, tnum, opt, num_threads;
    struct thread_info *tinfo;
    pthread_attr_t attr;
    int stack_size;
    void *res;

    /* The "-s" option specifies a stack size for our threads */
    /* per fare il parsing degli argomenti passati al main e usati  dal thread viene  usata la  funzione getopt(3). Individua le opzioni  precedute da  - e -- ed eventuali valori delle opzioni,  ad es: -s 0x200000

    int getopt(int argc, char * const argv[],
              const char *optstring);


*/
    extern char *optarg;
    extern int optind, opterr, optopt;
    stack_size = -1;
    while ((opt = getopt(argc, argv, "s:")) != -1)
    { // :  significa che e' un opzione seguita da un valore ritornato in optarg)
        switch (opt)
        {
        case 's':
            stack_size = strtoul(optarg, NULL, 0);
            break;

        default:
            fprintf(stderr, "Usage: %s [-s stack-size] arg...\n",
                    argv[0]);
            exit(EXIT_FAILURE);
        }
    }

    num_threads = argc - optind; /* optind e' l'indice del
     prossimo argomento da processare in argv. Se ad es:
        argv=[prog_name, -s, stacksize, w1, w2, w3]
        argc=6
        optind=3 */

    /* Initialize thread creation attributes */

    s = pthread_attr_init(&attr);
    if (s != 0)
        handle_error_en(s, "pthread_attr_init");

    if (stack_size > 0)
    {
        s = pthread_attr_setstacksize(&attr, stack_size);
        if (s != 0)
            handle_error_en(s, "pthread_attr_setstacksize");
    }

    /* Allocate memory for pthread_create() arguments */

    tinfo = calloc(num_threads, sizeof(struct thread_info));
    if (tinfo == NULL)
        handle_error("calloc");

    /* Create one thread for each command-line argument */

    for (tnum = 0; tnum < num_threads; tnum++)
    {
        tinfo[tnum].thread_num = tnum + 1;
        tinfo[tnum].argv_string = argv[optind + tnum];

        /* The pthread_create() call stores the thread ID into
           corresponding element of tinfo[] */

        s = pthread_create(&tinfo[tnum].thread_id, &attr,
                           &thread_start, &tinfo[tnum]);
        if (s != 0)
            handle_error_en(s, "pthread_create");
    }

    /* Destroy the thread attributes object, since it is no
       longer needed */

    s = pthread_attr_destroy(&attr);
    if (s != 0)
        handle_error_en(s, "pthread_attr_destroy");

    /* Now join with each thread, and display its returned value */

    for (tnum = 0; tnum < num_threads; tnum++)
    {
        s = pthread_join(tinfo[tnum].thread_id, &res);
        if (s != 0)
            handle_error_en(s, "pthread_join");

        printf("Joined with thread %d; returned value was %s\n",
               tinfo[tnum].thread_num, (char *)res);
        free(res); /* Free memory allocated by thread */
    }

    free(tinfo);
    exit(EXIT_SUCCESS);
}
