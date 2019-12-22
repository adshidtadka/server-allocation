#pragma once
#include <vector>

class Sum {
    int user_num, serv_num, cap, delay_max;
    int **delays, **edges, **edges_copy;
    int used_server_one;
    std::vector<int> used_server_mul;

public:
    void readInput();
    void startAlgo();
    int oneServer();
    int mulServer();
    void copyServer();
};