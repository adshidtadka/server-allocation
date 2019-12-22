#include "hopcroft_karp.hpp"

int main() {
    int leftNum, rightNum, edgeNum;
    std::cin >> leftNum >> rightNum >> edgeNum;
    // vertices of left side, right side and edges
    HopcroftKarp hc(leftNum, rightNum);
    int u, v;
    for (int i = 0; i < edgeNum; ++i) {
        std::cin >> u >> v;
        hc.addEdge(u, v);
    }

    int res = hc.matching();
    std::cout << "Maximum matching is " << res << "\n";

    return 0;
}
