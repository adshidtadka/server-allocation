#include <chrono>
#include <fstream>
#include <iostream>

#include "sum.hpp"

using namespace std;

const int INF = 99999999;

void Sum::readInput() {
    ifstream fin;
    fin.open("../../tmp/input.txt");
    if (!fin) {
        cout << "../../tmp/input.txt does not exist" << endl;
    }
    fin >> userNum >> serverNum >> capacity >> delayMax;

    delays = new int *[userNum + 1];
    for (int i = 0; i < userNum; i++) {
        delays[i] = new int[serverNum + 1];
        for (int j = 0; j < serverNum; j++) {
            int delay;
            fin >> delay;
            delays[i][j] = delay;
        }
    }

    edges = new int *[userNum * serverNum + 1];
    for (int i = 0; i < userNum * serverNum; i++) {
        edges[i] = new int[4];
        int u, s, d;
        fin >> u >> s >> d;
        edges[i][0] = u;
        edges[i][1] = s;
        edges[i][2] = d;
    }
}

void Sum::startAlgo() {
    chrono::system_clock::time_point start = chrono::system_clock::now();
    int solutionOne = oneServer();
    int solutionMultiple = mulServer();
    chrono::system_clock::time_point end = chrono::system_clock::now();
    int diffMs =
        chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << diffMs << " [ms]\n";
}

int Sum::oneServer() {
    // allocate all user and get max d_u for each server
    int delayMaxs[serverNum + 1];
    for (int i = 0; i < serverNum; i++) {
        if (capacity >= userNum) {
            int delayMax = 0;
            for (int j = 0; j < userNum; j++) {
                delayMax = delays[j][i] > delayMax ? delays[j][i] : delayMax;
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
            usedServerOne = i;
        }
    }
    return delayMin;
}

int Sum::mulServer() {
    copyServer();

    return 0;
}

void Sum::copyServer() {
    // add edges depending on capacity
    edgesCopy = new int *[userNum * serverNum * capacity + 1];
    for (int i = 0; i < userNum * serverNum; i++) {
        for (int j = 1; j <= capacity; j++) {
            edgesCopy[i * j] = new int[4];
            edgesCopy[i * j][0] = edges[i][0];
            edgesCopy[i * j][1] = edges[i][1];
            edgesCopy[i * j][2] = edges[i][2];
        }
    }
}