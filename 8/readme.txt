running make clean check on the unmodfied
SRT resulted int he following output:
time ./srt 1-test.ppm >1-test.ppm.tmp

real    0m48.688s
user    0m48.703s
sys     0m0.002s
mv 1-test.ppm.tmp 1-test.ppm
time ./srt 2-test.ppm >2-test.ppm.tmp
./srt: Multithreading is not supported yet.

real    0m0.002s
user    0m0.000s
sys     0m0.001s
Makefile:36: recipe for target '2-test.ppm' failed
make: *** [2-test.ppm] Error 1

After making changes with the goal to increase the output of
make clean check is:

time ./srt 1-test.ppm >1-test.ppm.tmp

real    0m48.448s
user    0m48.463s
sys     0m0.001s
mv 1-test.ppm.tmp 1-test.ppm
time ./srt 2-test.ppm >2-test.ppm.tmp

real    0m24.712s
user    0m49.095s
sys     0m0.003s
mv 2-test.ppm.tmp 2-test.ppm
time ./srt 4-test.ppm >4-test.ppm.tmp

real    0m12.484s
user    0m49.225s
sys     0m0.003s
mv 4-test.ppm.tmp 4-test.ppm
time ./srt 8-test.ppm >8-test.ppm.tmp

real    0m6.598s
user    0m50.944s
sys     0m0.003s
mv 8-test.ppm.tmp 8-test.ppm
for file in 1-test.ppm 2-test.ppm 4-test.ppm 8-test.ppm; do \
  diff -u baseline.ppm $file || exit; \
done

These results clearly show that increasing the threads improves
the speed of the program as 2 threads results in half the real time,
4 threads results in a 4th the real time and 8 threads results in an eighth.

The only trouble I ran into during this assignment was determining a plan of 
action to reduce the time. However once a solid plan was found to start
everything went smoothly.