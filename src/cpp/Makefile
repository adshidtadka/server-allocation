run_sum: run_sum.o sum.o hopcroft_karp.o
	g++ -Wall -o run_sum.out run_sum.o sum.o hopcroft_karp.o
hopcroft_karp.o: hopcroft_karp.cpp
	g++ -Wall -c hopcroft_karp.cpp
sum.o: sum.cpp
	g++ -Wall -c sum.cpp
run_sum.o: run_sum.cpp
	g++ -Wall -c run_sum.cpp
clean:
	rm -f *.o run_sum