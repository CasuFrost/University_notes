CFLAGS := -O2
CC := gcc
main : main.o checkIfPal.o leggi.o
	$(CC) $^ -o $@

%.o : %.c

	$(CC) $(CFLAGS) -c $< -o $@