#pragma once

#include <vector>

class Sum {
    int userNum, serverNum, capacity, delayMax;
    int **userDelays, **userEdges, **serverEdges, **userEdgesCopy;
    int *matchedServers;
    int cpuTime, solMax, solMin;

public:
    void readInput();
    void startAlgo();
    int oneServer();
    int multipleServer();
    void copyServer();
};