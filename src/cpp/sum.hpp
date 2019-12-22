#pragma once

#include <vector>

class Sum {
    int userNum, serverNum, capacity, delayMax;
    int **delays, **edges, **edgesCopy;
    int usedServerOne;
    std::vector<int> usedServerMultiple;

public:
    void readInput();
    void startAlgo();
    int oneServer();
    int multipleServer();
    void copyServer();
};