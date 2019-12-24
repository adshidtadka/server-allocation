#include <chrono>
#include <fstream>
#include <iostream>

#include "hopcroft_karp.hpp"
#include "sum.hpp"

using namespace std;

const int INF = 99999999;

void Sum::readInput() {
    ifstream fin;
    fin.open("../../tmp/input.txt");
    if (!fin) {
        cout << "../../tmp/input.txt does not exist" << endl;
    }
    fin >> userNum >> serverNum >> capacity >> userDelayMax >> serverDelayMin;

    userDelays = new int *[userNum + 1];
    for (int i = 0; i < userNum; i++) {
        userDelays[i] = new int[serverNum + 1];
        for (int j = 0; j < serverNum; j++) {
            int delay;
            fin >> delay;
            userDelays[i][j] = delay;
        }
    }

    serverDelays = new int *[serverNum + 1];
    for (int i = 0; i < serverNum; i++) {
        serverDelays[i] = new int[serverNum + 1];
        for (int j = 0; j < serverNum; j++) {
            int delay;
            fin >> delay;
            serverDelays[i][j] = delay;
        }
    }

    userEdges = new int *[userNum * serverNum + 1];
    for (int i = 0; i < userNum * serverNum; i++) {
        userEdges[i] = new int[3];
        int u, s, d;
        fin >> u >> s >> d;
        userEdges[i][0] = u;
        userEdges[i][1] = s;
        userEdges[i][2] = d;
    }
}

void Sum::startAlgo() {
    chrono::system_clock::time_point start = chrono::system_clock::now();

    int userDelayOne = oneServer();
    int userDelayMul = multipleServer();

    if (userDelayMul < userDelayOne) {
        solMin = userDelayMul * 2 + serverDelayMin;
        solMax = INF;
        // for (int i = 0; i < userNum; i++) {
        //     for (int j = 0; j < userNum; j++) {
        //         int serverX = matchedServers[i] % serverNum;
        //         int serverY = matchedServers[j] % serverNum;
        //         // if (serverX != serverY && ed)
        //         // {
        //         //     /* code */
        //         // }
        //     }
        // }

    } else {
        solMin, solMax = userDelayOne * 2;
    }

    chrono::system_clock::time_point end = chrono::system_clock::now();

    cpuTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
    cout << cpuTime << " [μs]\n";
}

int Sum::oneServer() {
    // allocate all user and get max d_u for each server
    int delayMaxs[serverNum + 1];
    for (int i = 0; i < serverNum; i++) {
        if (capacity >= userNum) {
            int delayMax = 0;
            for (int j = 0; j < userNum; j++) {
                delayMax =
                    userDelays[j][i] > delayMax ? userDelays[j][i] : delayMax;
            }
            delayMaxs[i] = delayMax;
        } else {
            delayMaxs[i] = INF;
        }
    }

    // search minimum d_u
    int delayMin = INF;
    for (int i = 0; i < serverNum; i++) {
        if (delayMaxs[i] < delayMin) {
            delayMin = delayMaxs[i];
        }
    }
    return delayMin;
}

int Sum::multipleServer() {
    copyServer();

    // search matching
    for (int i = 1; i <= userDelayMax; i++) {
        HopcroftKarp hc(userNum, serverNum * capacity);
        for (int j = 0; j < userNum * serverNum * capacity; j++) {
            if (userEdgesCopy[j][2] <= i) {
                hc.addEdge(userEdgesCopy[j][0], userEdgesCopy[j][1]);
            }
        }
        if (hc.matching() == userNum) {
            matchedServers = new int[userNum];
            matchedServers = hc.getMatched(matchedServers);
            return i;
        }
    }

    return INF;
}

void Sum::copyServer() {
    // add userEdges depending on capacity
    userEdgesCopy = new int *[userNum * serverNum * capacity + 1];
    for (int i = 0; i < userNum * serverNum * capacity; i++) {
        userEdgesCopy[i] = new int[4];
        int serverNumCopied = serverNum * capacity;
        int u = i / serverNumCopied;
        int s = i % serverNumCopied;
        userEdgesCopy[i][0] = u;
        userEdgesCopy[i][1] = s;
        userEdgesCopy[i][2] = userEdges[u][s % serverNum];
    }
}