#include "esum.hpp"

int main() {
    Esum esum;
    esum.readInput();
    // esum.createServerEdges();
    esum.startAlgo();
    esum.writeOutput();
    return 0;
}