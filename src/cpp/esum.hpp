#pragma once

#include "sum.hpp"

class Esum : public Sum {
public:
    int **createServerEdges();
    void startAlgo();
    int multipleServer();
};
