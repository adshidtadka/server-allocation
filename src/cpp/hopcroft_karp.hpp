#pragma once

#include <list>

// A class to represent Bipartite graph for
// Hopcroft Karp implementation
class HopcroftKarp {
    // leftNum and rightNum are number of vertices on left
    // and right sides of Bipartite Graph
    int leftNum, rightNum;

    // adjacent[u] stores adjacents of left side
    // vertex 'u'. The value of u ranges from 1 to leftNum.
    // 0 is used for dummy vertex
    std::list<int> *adjacent;

    // pointers for hopcroftKarp()
    int *uPair, *vPair, *distance;

public:
    HopcroftKarp(int leftNum, int rightNum);  // Constructor
    void addEdge(int u, int v);               // To add edge

    // Returns true if there is an augmenting path
    bool bfs();

    // Adds augmenting path if there is one beginning
    // with u
    bool dfs(int u);

    // Returns size of maximum matching
    int matching();
};