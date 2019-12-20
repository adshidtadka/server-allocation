#include <fstream>
#include <iostream>
using namespace std;

class Sum {
    int user_num, server_num, edges_num, delay_max;
    int *caps, **edges;

public:
    void read_input();
};

void Sum::read_input() {
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

int main() {
    Sum sum;
    sum.read_input();
    return 0;
}