#ifndef dtmc_h
#define dtmc_h

#include "main.h"


typedef double state_type;
typedef double input_type;
typedef double output_type;


class DTMC {

private:

  RandGen *p;  // pointer to random generator class
  
  void dtmc_body(RandGen *p);

public:

  int STATE_SIZE = 2; // state size
  int INPUT_SIZE = 2; // input size
  int OUTPUT_SIZE = 2; // output size

  state_type *x;  // present state
  input_type *u;  // input
  output_type *y;  // output

  DTMC(RandGen *p);
  DTMC(int xsize, int usize, int ysize, RandGen *p);

  // define initial state
  void init();

  // update state
  void next();
  
  // update output
  void output();

  // print log on stdout
  void printlog(int t);

  // print log on file
  void fprintflog(FILE *fp, int t);
};


#endif
