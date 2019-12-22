run_sum: run_sum.o sum.o
	g++ -Wall -o run_sum run_sum.o sum.o
sum.o: sum.cpp
	g++ -Wall -c sum.cpp
run_sum.o: run_sum.cpp
	g++ -Wall -c run_sum.cpp
clean:
	rm -f *.o run_sum