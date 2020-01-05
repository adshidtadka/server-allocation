#pragma once

#include <vector>

class Sum {
protected:
    const static int INF = 99999999;
    int userNum, servNum, capacity, userDelayMax, servDelayMin, servDelayMax;
    int **userDelays, **servDelays;
    int **userEdges;
    int *matchedServers;
    int cpuTime, solMax, solMin;

public:
    void readInput();
    void writeOutput();
    void startAlgo();
    int oneServer();
    int multipleServer(std::vector<int>);
    int **copyServer();
};