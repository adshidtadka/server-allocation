#include <chrono>
#include <fstream>
#include <iostream>

using namespace std;

class Sum {
    int user_num, server_num, edges_num, delay_max;
    int *caps, **delays, **edges;

public:
    void readInput();
    void startAlgo();
    int oneServer();
};

void Sum::readInput() {
    ifstream fin;
    fin.open("../tmp/input.txt");
    if (!fin) {
        cout << "../tmp/input.txt does not exist" << endl;
    }
    fin >> user_num >> server_num >> edges_num >> delay_max;

    caps = new int[server_num + 1];
    for (int i = 0; i < server_num; i++) {
        int cap;
        fin >> cap;
        caps[i] = cap;
    }

    delays = new int *[user_num + 1];
    for (int i = 0; i < user_num; i++) {
        delays[i] = new int[server_num + 1];
        for (int j = 0; j < server_num; j++) {
            int delay;
            fin >> delay;
            delays[i][j] = delay;
        }
    }

    edges = new int *[edges_num + 1];
    for (int i = 0; i < edges_num; i++) {
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
    chrono::system_clock::time_point end = chrono::system_clock::now();
    int dif_ms =
        chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << dif_ms << " [ms]\n";
}

int Sum::oneServer() {
    // allocate all user and get max d_u
    int delay_maxs[server_num + 1];
    // for (int i = 0; i < server_num; i++) {
    //     if (caps[i] >= user_num) {
    //         int delay_max = 0;
    //         for (int j = 0; j < user_num; j++) {
    //             delay_max = edges[]
    //         }
    //     }
    // }
    return 0;
}

int main() {
    Sum sum;
    sum.readInput();
    sum.startAlgo();
    return 0;
}