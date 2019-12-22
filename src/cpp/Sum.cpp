#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

const int INF = 99999999;

class Sum {
    int user_num, serv_num, cap, delay_max;
    int **delays, **edges, **edges_copy;
    int used_server_one;
    vector<int> used_server_mul;

public:
    void readInput();
    void startAlgo();
    int oneServer();
    int mulServer();
    void copyServer();
};

void Sum::readInput() {
    ifstream fin;
    fin.open("../../tmp/input.txt");
    if (!fin) {
        cout << "../../tmp/input.txt does not exist" << endl;
    }
    fin >> user_num >> serv_num >> cap >> delay_max;

    delays = new int *[user_num + 1];
    for (int i = 0; i < user_num; i++) {
        delays[i] = new int[serv_num + 1];
        for (int j = 0; j < serv_num; j++) {
            int delay;
            fin >> delay;
            delays[i][j] = delay;
        }
    }

    edges = new int *[user_num * serv_num + 1];
    for (int i = 0; i < user_num * serv_num; i++) {
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
    int sol_one_server = oneServer();
    int mul_server = mulServer();
    chrono::system_clock::time_point end = chrono::system_clock::now();
    int dif_ms =
        chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << dif_ms << " [ms]\n";
}

int Sum::oneServer() {
    // allocate all user and get max d_u for each server
    int delay_maxs[serv_num + 1];
    for (int i = 0; i < serv_num; i++) {
        if (cap >= user_num) {
            int delay_max = 0;
            for (int j = 0; j < user_num; j++) {
                delay_max = delays[j][i] > delay_max ? delays[j][i] : delay_max;
            }
            delay_maxs[i] = delay_max;
        } else {
            delay_maxs[i] = INF;
        }
    }

    // search minimum d_u
    int delay_min = INF;
    for (int i = 0; i < serv_num; i++) {
        if (delay_maxs[i] < delay_min) {
            delay_min = delay_maxs[i];
            used_server_one = i;
        }
    }
    return delay_min;
}

int Sum::mulServer() {
    copyServer();

    return 0;
}

void Sum::copyServer() {
    // add edges depending on capacity
    edges_copy = new int *[user_num * serv_num * cap + 1];
    for (int i = 0; i < user_num * serv_num; i++) {
        for (int j = 1; j <= cap; j++) {
            edges_copy[i * j] = new int[4];
            edges_copy[i * j][0] = edges[i][0];
            edges_copy[i * j][1] = edges[i][1];
            edges_copy[i * j][2] = edges[i][2];
        }
    }
}

int main() {
    Sum sum;
    sum.readInput();
    sum.startAlgo();
    return 0;
}