// C++ implementation of Hopcroft Karp algorithm for
// maximum matching
#include <climits>
#include <cstdlib>
#include <iostream>
#include <queue>

#include "hopcroft_karp.hpp"

const int NIL = 0;
const int INF = INT_MAX;

// Returns size of maximum matching
int HopcroftKarp::matching() {
    // uPair[u] stores pair of u in matching on left side of Bipartite Graph.
    // If u doesn't have any pair, then uPair[u] is NIL
    uPair = new int[leftNum + 1];

    // vPair[v] stores pair of v in matching on right side of Bipartite Graph.
    // If v doesn't have any pair, then uPair[v] is NIL
    vPair = new int[rightNum + 1];

    // distance[u] stores distance of left side vertices
    distance = new int[leftNum + 1];

    // Initialize NIL as pair of all vertices
    for (int u = 0; u <= leftNum; u++) uPair[u] = NIL;
    for (int v = 0; v <= rightNum; v++) vPair[v] = NIL;

    // Initialize result
    int result = 0;

    // Keep updating the result while there is an
    // augmenting path possible.
    while (bfs()) {
        // Find a free vertex to check for a matching
        for (int u = 1; u <= leftNum; u++)

            // If current vertex is free and there is
            // an augmenting path from current vertex
            // then increment the result
            if (uPair[u] == NIL && dfs(u)) result++;
    }
    return result;
}

int *HopcroftKarp::getMatched(int *matched) {
    memcpy(matched, uPair, sizeof(int) * leftNum);
    return matched;
}

// Returns true if there is an augmenting path available, else returns false
bool HopcroftKarp::bfs() {
    std::queue<int> q;  // an integer queue for bfs

    // First layer of vertices (set distance as 0)
    for (int u = 1; u <= leftNum; u++) {
        // If this is a free vertex, add it to queue
        if (uPair[u] == NIL) {
            // u is not matched so distance is 0
            distance[u] = 0;
            q.push(u);
        }

        // Else set distance as infinite so that this vertex is considered
        // next time for availability
        else
            distance[u] = INF;
    }

    // Initialize distance to NIL as infinite
    distance[NIL] = INF;

    // q is going to contain vertices of left side only.
    while (!q.empty()) {
        // dequeue a vertex
        int u = q.front();
        q.pop();

        // If this node is not NIL and can provide a shorter path to NIL then
        if (distance[u] < distance[NIL]) {
            // Get all the adjacent vertices of the dequeued vertex u
            std::list<int>::iterator it;
            for (it = adjacent[u].begin(); it != adjacent[u].end(); ++it) {
                int v = *it;

                // If pair of v is not considered so far
                // i.edgeNum. (v, vPair[v]) is not yet explored edge.
                if (distance[vPair[v]] == INF) {
                    // Consider the pair and push it to queue
                    distance[vPair[v]] = distance[u] + 1;
                    q.push(vPair[v]);
                }
            }
        }
    }

    // If we could come back to NIL using alternating path of distance
    // vertices then there is an augmenting path available
    return (distance[NIL] != INF);
}

// Returns true if there is an augmenting path beginning with free vertex u
bool HopcroftKarp::dfs(int u) {
    if (u != NIL) {
        std::list<int>::iterator it;
        for (it = adjacent[u].begin(); it != adjacent[u].end(); ++it) {
            // Adjacent vertex of u
            int v = *it;

            // Follow the distance set by BFS search
            if (distance[vPair[v]] == distance[u] + 1) {
                // If dfs for pair of v also return true then
                if (dfs(vPair[v]) == true) {
                    // new matching possible, store the matching
                    vPair[v] = u;
                    uPair[u] = v;
                    return true;
                }
            }
        }

        // If there is no augmenting path beginning with u then.
        distance[u] = INF;
        return false;
    }
    return true;
}

// Constructor for initialization
HopcroftKarp::HopcroftKarp(int leftNum, int rightNum) {
    this->leftNum = leftNum;
    this->rightNum = rightNum;
    adjacent = new std::list<int>[leftNum + 1];
}

// Destructor
HopcroftKarp::~HopcroftKarp() {
    adjacent.~list<int>();
    delete[] uPair;
    delete[] vPair;
    delete[] distance;
}

// function to add edge from u to v
void HopcroftKarp::addEdge(int u, int v) {
    adjacent[u + 1].push_back(v + 1);  // Add v to u’s list.
}
