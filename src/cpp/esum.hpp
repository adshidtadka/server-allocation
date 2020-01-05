#pragma once

#include "sum.hpp"

class Esum : public Sum {
    int solOpt;

public:
    void startAlgo();
    int multipleServer();
    void writeOutput();
};
