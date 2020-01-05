#ifndef BRON_KERBOSCH_UTILS_H
#define BRON_KERBOSCH_UTILS_H

#include "bron-kerbosch.h"

namespace BronKerbosch {

template <typename T>
bool edge(Graph<T>& G, const T& a, const T& b) {
    auto ai = std::find_if(G.begin(), G.end(),
                           [&](const Vertex<T>& v) { return v.id == a; });
    auto bi = std::find_if(G.begin(), G.end(),
                           [&](const Vertex<T>& v) { return v.id == b; });
    if (G.end() != ai && G.end() != bi) {
        ai->ns.insert(b);
        bi->ns.insert(a);

        return true;
    }

    return false;
};

template <typename T>
Graph<T> complement(const Graph<T>& G) {
    Graph<T> N = G;

    std::forward_list<T> a;
    for (const auto& v : G) {
        a.push_front(v.id);
    }

    for (auto& v : N) {
        const auto t = v.ns;
        v.ns.clear();
        for (const auto& b : a) {
            if (v.id != b && t.end() == std::find(t.begin(), t.end(), b)) {
                v.ns.insert(b);
            }
        }
    }

    return N;
}

}  // namespace BronKerbosch

#endif  // BRON_KERBOSCH_UTILS_H
