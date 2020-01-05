#include <iostream>

#include "bron-kerbosch.hpp"
#include "bron-kerbosch_utils.hpp"

using namespace BronKerbosch;
using namespace std::placeholders;
template <typename T>
using Solution = std::forward_list<Graph<T> >;

int main() {
    // Arrange.
    Graph<int> P;
    P.push_front({0});
    P.push_front({1});
    P.push_front({2});
    P.push_front({3});
    P.push_front({4});
    P.push_front({5});
    edge<int>(P, 0, 1);
    edge<int>(P, 0, 2);
    edge<int>(P, 0, 3);
    edge<int>(P, 1, 2);
    edge<int>(P, 1, 3);
    edge<int>(P, 1, 4);
    edge<int>(P, 1, 5);
    edge<int>(P, 2, 3);
    edge<int>(P, 2, 4);
    edge<int>(P, 2, 5);
    edge<int>(P, 3, 4);
    edge<int>(P, 3, 5);
    edge<int>(P, 4, 5);

    Solution<int> solution;
    const auto act = [&solution](Graph<int> R, Graph<int>, Graph<int>) {
        solution.push_front(R);
    };

    // Act.
    solve<int>({{}}, P, {{}}, act);

    // Print.
    for (const auto& g : solution) {
        for (const auto& v : g) std::cout << v.id << " ";
        std::cout << std::endl;
    }

    return 0;
}