#include <chrono>
#include <fstream>
#include <iostream>

#include "bron-kerbosch_utils.hpp"
#include "esum.hpp"

using namespace std;
using namespace BronKerbosch;

void Esum::startAlgo() {
    chrono::system_clock::time_point start = chrono::system_clock::now();

    int totalDelayOne = oneServer() * 2;
    int totalDelayMul = Esum::multipleServer();

    solMin = solMax =
        totalDelayOne <= totalDelayMul ? totalDelayOne : totalDelayMul;

    chrono::system_clock::time_point end = chrono::system_clock::now();
    cpuTime = chrono::duration_cast<chrono::microseconds>(end - start).count();

    cout << "solMin = " << solMin << endl;
    cout << "cpuTime = " << cpuTime << endl;
}

int Esum::multipleServer() { return INF; }