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
    fin >> userNum >> servNum >> capacity >> userDelayMax >> servDelayMin;

    userDelays = new int *[userNum + 1];
    for (int i = 0; i < userNum; i++) {
        userDelays[i] = new int[servNum + 1];
        for (int j = 0; j < servNum; j++) {
            int delay;
            fin >> delay;
            userDelays[i][j] = delay;
        }
    }

    servDelays = new int *[servNum + 1];
    for (int i = 0; i < servNum; i++) {
        servDelays[i] = new int[servNum + 1];
        for (int j = 0; j < servNum; j++) {
            int delay;
            fin >> delay;
            servDelays[i][j] = delay;
        }
    }

    userEdges = new int *[userNum * servNum + 1];
    for (int i = 0; i < userNum * servNum; i++) {
        userEdges[i] = new int[3];
        int u, s, d;
        fin >> u >> s >> d;
        userEdges[i][0] = u;
        userEdges[i][1] = s;
        userEdges[i][2] = d;
    }
}

void Sum::writeOutput() {
    ofstream fout;
    fout.open("../../tmp/output.txt");

    fout << cpuTime << " " << solMin << " " << solMax << endl;
}

void Sum::startAlgo() {
    chrono::system_clock::time_point start = chrono::system_clock::now();

    int userDelayOne = oneServer();
    int userDelayMul = multipleServer();

    if (userDelayOne <= userDelayMul) {
        solMin = solMax = userDelayOne * 2;
    } else {
        solMin = userDelayMul * 2 + servDelayMin;
        int servDelayMax = 0;
        for (int i = 0; i < userNum; i++) {
            for (int j = 0; j < userNum; j++) {
                int s = matchedServers[i];
                int t = matchedServers[j];
                servDelayMax = servDelays[s][t] > servDelayMax
                                   ? servDelays[s][t]
                                   : servDelayMax;
            }
        }
        solMax = userDelayMul * 2 + servDelayMax;
    }

    chrono::system_clock::time_point end = chrono::system_clock::now();
    cpuTime = chrono::duration_cast<chrono::microseconds>(end - start).count();
}

int Sum::oneServer() {
    // allocate all user and get max d_u for each server
    int delayMaxs[servNum + 1];
    for (int i = 0; i < servNum; i++) {
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
    for (int i = 0; i < servNum; i++) {
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
        HopcroftKarp hc(userNum, servNum * capacity);
        for (int j = 0; j < userNum * servNum * capacity; j++) {
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
    userEdgesCopy = new int *[userNum * servNum * capacity + 1];
    for (int i = 0; i < userNum * servNum * capacity; i++) {
        userEdgesCopy[i] = new int[4];
        int servNumCopied = servNum * capacity;
        int u = i / servNumCopied;
        int s = i % servNumCopied;
        userEdgesCopy[i][0] = u;
        userEdgesCopy[i][1] = s;
        userEdgesCopy[i][2] = userEdges[u][s % servNum];
    }
}