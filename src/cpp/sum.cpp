#include <algorithm>
#include <chrono>
#include <fstream>
#include <vector>

#include <iostream>

#include "hopcroft-karp.hpp"
#include "sum.hpp"

using namespace std;

void Sum::readInput() {
    ifstream fin;
    fin.open("../../tmp/input.txt");
    if (!fin) {
        cout << "../../tmp/input.txt does not exist" << endl;
    }
    fin >> userNum >> servNum >> capacity >> userDelayMax >> servDelayMin >>
        servDelayMax;

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

    userEdges = createUserEdges();
}

void Sum::writeOutput() {
    ofstream fout;
    fout.open("../../tmp/output.txt");

    fout << cpuTime << " " << solMin << " " << solMax << endl;
}

void Sum::startAlgo() {
    chrono::system_clock::time_point start = chrono::system_clock::now();

    int userDelayOne = oneServer();
    // available all server
    vector<int> v;
    for (int i = 0; i < servNum; i++) {
        v.push_back(i);
    }
    int userDelayMul = multipleServer(v);

    if (userDelayOne <= userDelayMul) {
        solMin = solMax = userDelayOne * 2;
    } else {
        solMin = userDelayMul * 2 + servDelayMin;
        int servDelayMax = 0;
        for (int i = 0; i < userNum; i++) {
            for (int j = 0; j < userNum; j++) {
                int s = matchedServers[i] % servNum;
                int t = matchedServers[j] % servNum;
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

int Sum::multipleServer(vector<int> v) {
    // push_back copied server
    int availServNum = v.size();
    for (int i = 0; i < availServNum; i++) {
        for (int j = 1; j < capacity; j++) {
            v.push_back(v[i] + servNum * j);
        }
    }

    HopcroftKarp hc(userNum, servNum * capacity);
    for (int i = 1; i <= userDelayMax; i++) {
        for (int j = 0; j < userNum * servNum * capacity; j++) {
            int servNode = userEdges[j][1];
            if (userEdges[j][2] == i &&
                find(v.begin(), v.end(), servNode) != v.end()) {
                hc.addEdge(userEdges[j][0], servNode);
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

int **Sum::createUserEdges() {
    // add userEdges depending on capacity
    int **userEdges = new int *[userNum * servNum * capacity + 1];
    for (int i = 0; i < userNum * servNum * capacity; i++) {
        userEdges[i] = new int[3];
        int servNumCopied = servNum * capacity;
        int u = i / servNumCopied;
        int s = i % servNumCopied;
        userEdges[i][0] = u;
        userEdges[i][1] = s;
        userEdges[i][2] = userDelays[u][s % servNum];
    }
    return userEdges;
}