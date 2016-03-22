CC = gcc
CFLAGS = -g3 -Wall -Wextra -march=native -mtune=native -mrdrnd

randmain: randmain.o randcpuid.o
	$(CC) $(CFLAGS) -o randmain randmain.o randcpuid.o -ldl -Wl,-rpath=$(PWD)

randmain.o: randmain.c
	$(CC) $(CFLAGS) -o randmain.o -c randmain.c

randcpuid.o: randcpuid.c
	$(CC) $(CFLAGS) -o randcpuid.o -c randcpuid.c

randlibhw.so: randlibhw.o
	$(CC) $(CFLAGS) -shared randlibhw.o -o randlibhw.so

randlibhw.o: randlibhw.c
	$(CC) $(CFLAGS) -fPIC -o randlibhw.o -c randlibhw.c

randlibsw.so: randlibsw.o
	$(CC) $(CFLAGS) -shared randlibsw.o -o randlibsw.so

randlibsw.o: randlibsw.c
	$(CC) $(CFLAGS) -fPIC -o randlibsw.o -c randlibsw.c
