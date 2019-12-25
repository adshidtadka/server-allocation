#pragma once

#include <vector>

class Sum {
    int userNum, servNum, capacity, userDelayMax, servDelayMin;
    int **userDelays, **servDelays;
    int *matchedServers;
    int cpuTime, solMax, solMin;

public:
    void readInput();
    void writeOutput();
    void startAlgo();
    int oneServer();
    int multipleServer();
    int **copyServer();
};