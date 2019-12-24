#include <chrono>
#include <iostream>
#include "sum.hpp"

int main() {
    std::chrono::system_clock::time_point start =
        std::chrono::system_clock::now();
    Sum sum;
    sum.readInput();
    sum.startAlgo();
    sum.writeOutput();
    std::chrono::system_clock::time_point end =
        std::chrono::system_clock::now();
    float cpuTime =
        float(std::chrono::duration_cast<std::chrono::microseconds>(end - start)
                  .count()) /
        1000 / 1000;
    std::cout << "cpuTime from cpp " << cpuTime << " [s]\n";
    return 0;
}