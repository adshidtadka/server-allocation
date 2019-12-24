#pragma once

#include <vector>

class Sum {
    int userNum, servNum, capacity, userDelayMax, servDelayMin;
    int **userDelays, **userEdges, **servDelays, **userEdgesCopy;
    int *matchedServers;
    int cpuTime, solMax, solMin;

public:
    void readInput();
    void startAlgo();
    int oneServer();
    int multipleServer();
    void copyServer();
};