#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

class Sum {
    int user_num, server_num, edges_num, delay_max;
    int *caps, **edges;

public:
    void readInput();
    void startAlgo();
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

    edges = new int *[edges_num + 1];
    for (int i = 0; i < edges_num; i++) {
        edges[i] = new int[3];
        int u, s, d;
        fin >> u >> s >> d;
        edges[i][0] = u;
        edges[i][1] = s;
        edges[i][2] = d;
    }
}

void Sum::startAlgo() {
    const int N = 1000 * 1000;
    std::vector<int> v;
    auto start = chrono::system_clock::now();
    for (int i = 0; i < N; i++) {
        v.push_back(i);
    }
    auto end = chrono::system_clock::now();
    auto dif_ms =
        chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << dif_ms << " [ms]\n";
}

int main() {
    Sum sum;
    sum.readInput();
    sum.startAlgo();
    return 0;
}