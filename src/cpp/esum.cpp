#include <chrono>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>

#include "bron-kerbosch_utils.hpp"
#include "esum.hpp"

using namespace std;
using namespace BronKerbosch;

template <typename T>
using Solution = std::forward_list<Graph<T>>;

void Esum::startAlgo() {
    serverEdges = createServerEdges();
    chrono::system_clock::time_point start = chrono::system_clock::now();

    int totalDelayOne = oneServer() * 2;
    int totalDelayMul = Esum::multipleServer();

    solMin = solMax =
        totalDelayOne <= totalDelayMul ? totalDelayOne : totalDelayMul;

    chrono::system_clock::time_point end = chrono::system_clock::now();
    cpuTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
}

int Esum::multipleServer() {
    // initialize server nodes
    Graph<int> G;
    for (int i = 0; i < servNum; i++) {
        G.push_front({i});
    }

    // record allocation
    set<vector<int>> nodesVecSet;
    int totalDelay = INF;

    // search clique
    for (int i = 1; i <= servDelayMax; i++) {
        for (int j = 0; j < servNum * (servNum - 1) / 2; j++) {
            if (serverEdges[j][2] == i)
                edge<int>(G, serverEdges[j][0], serverEdges[j][1]);
        }
        std::forward_list<Graph<int>> solution;
        const auto act = [&solution](Graph<int> R, Graph<int>, Graph<int>) {
            solution.push_front(R);
        };
        solve<int>({{}}, G, {{}}, act);
        for (const auto &g : solution) {
            vector<int> vec;
            for (const auto &vert : g) vec.push_back(vert.id);
            if (vec.size() > 1 && nodesVecSet.count(vec) == 0) {
                nodesVecSet.insert(vec);
                int totalDelayTmp = Sum::multipleServer(vec) * 2 + i;
                totalDelay =
                    totalDelayTmp < totalDelay ? totalDelayTmp : totalDelay;
            }
        }
    }
    return totalDelay;
}

int **Esum::createServerEdges() {
    int **serverEdges = new int *[servNum * (servNum - 1) / 2 + 1];
    int index = 0;
    for (int i = 0; i < servNum - 1; i++) {
        for (int j = i + 1; j < servNum; j++) {
            serverEdges[index] = new int[3];
            serverEdges[index][0] = i;
            serverEdges[index][1] = j;
            serverEdges[index][2] = servDelays[i][j];
            index++;
        }
    }
    return serverEdges;
}