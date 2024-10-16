#include "main.h"

#include "dtmc.h"


void DTMC::dtmc_body(RandGen *myp) {

  p = myp;
  
  if (STATE_SIZE <= 0)
    {
     fprintf(stderr, "DTMC(): Error: state size cannot be 0\n");
     exit(1);
    }
  
x = (state_type *) malloc(sizeof(state_type)*STATE_SIZE);

 if (x == NULL)
   {
     fprintf(stderr, "DTMC(): memory allocation for state failed\n");
     exit(1);
   }


  if (INPUT_SIZE <= 0)
    {
      u = NULL;
    }
  else
    {
 u = (input_type *) malloc(sizeof(input_type)*INPUT_SIZE);

 if (u == NULL)
   {
     fprintf(stderr, "DTMC(): memory allocation for input failed\n");
     exit(1);
   }
    } // if (INPUT_SIZE <= 0)
 
  if (OUTPUT_SIZE <= 0)
    {
     fprintf(stderr, "DTMC(): Error: output size cannot be 0\n");
     exit(1);
    }

  y = (output_type *) malloc(sizeof(output_type)*OUTPUT_SIZE);

 if (y == NULL)
   {
     fprintf(stderr, "DTMC(): memory allocation for output failed\n");
     exit(1);
   }


 
}



DTMC::DTMC(RandGen *myp)  {
  dtmc_body(myp);
}


DTMC::DTMC(int xsize, int usize, int ysize, RandGen *myp)  {

  STATE_SIZE = xsize;
  INPUT_SIZE = usize;
  OUTPUT_SIZE = ysize;

  dtmc_body(myp);
  
}


void DTMC::init() {

  /* initial state */

  int i;

  for (i = 0; i < STATE_SIZE; i++)
    {
      x[i] = 0;
    }
  

}  // init()



void DTMC::next() {

  /* update state */

  int i;

  for (i = 0; i < STATE_SIZE; i++)
    {
      x[i] = p -> get_random_double();
    }
  

} // next()


void DTMC::output() {

  /* update state */

  int i;

  for (i = 0; i < OUTPUT_SIZE; i++)
    {
      y[i] = x[i];
    }
}


void DTMC::printlog(int t) {

  /* update state */

  int i;

  printf("%d ", t);

  for (i = 0; i < STATE_SIZE; i++)
    {
      printf("%lf ", x[i]);
    }
  

  for (i = 0; i < OUTPUT_SIZE; i++)
    {
      printf("%lf ", y[i]);
    }

    for (i = 0; i < INPUT_SIZE; i++)
    {
      printf("%lf ", u[i]);
    }

   printf("\n");
   
} // next()


void DTMC::fprintflog(FILE *fp, int t) {

  /* update state */

  //  FILE *fp;
  int i;
  
  /*  prg  */

  //  fp = fopen(filename, "w");

  fprintf(fp, "%d ", t);

  for (i = 0; i < STATE_SIZE; i++)
    {
      fprintf(fp, "%lf ", x[i]);
    }
  

  for (i = 0; i < OUTPUT_SIZE; i++)
    {
      fprintf(fp, "%lf ", y[i]);
    }

    for (i = 0; i < INPUT_SIZE; i++)
    {
      fprintf(fp, "%lf ", u[i]);
    }

    fprintf(fp, "\n");
   
} // next()


