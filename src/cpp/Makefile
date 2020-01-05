run_sum: run_sum.o sum.o hopcroft-karp.o
	g++ -Wall -g  -o run_sum.out run_sum.o sum.o hopcroft-karp.o
run_esum: run_esum.o esum.o sum.o hopcroft-karp.o
	g++ -Wall -g  -o run_esum.out run_esum.o esum.o sum.o hopcroft-karp.o

hopcroft-karp.o: hopcroft-karp.cpp
	g++ -Wall -c -g hopcroft-karp.cpp
sum.o: sum.cpp
	g++ -Wall -c -g sum.cpp
run_sum.o: run_sum.cpp
	g++ -Wall -c -g run_sum.cpp
esum.o: esum.cpp
	g++ -Wall -c -g -std=c++11 esum.cpp
run_esum.o: run_esum.cpp
	g++ -Wall -c -g run_esum.cpp

clean:
	rm -f *.o run_sum run_esum