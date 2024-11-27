ALL:
	gcc -Wall -pedantic -g -fopenmp -o pi_estimation_openMP pi_estimation_openMP.c
	gcc -Wall -pedantic -g -fopenmp -o pi_estimation_serial pi_estimation_serial.c
	gcc -Wall -pedantic -g -fopenmp -o histogram histogram.c
	gcc -Wall -pedantic -g -fopenmp -o histogram_openMP histogram_openMP.c

a: 
	./histogram
	./histogram_openMP