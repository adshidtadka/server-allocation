# Finds all maximal cliques in a graph using the Bron-Kerbosch algorithm. The input graph here is
# in the adjacency list format, a dict with vertexes as keys and lists of their neighbors as values.
# https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm

from collections import defaultdict


class BronKerbosch():

    def __init__(self, server_num):
        self.graph = self.create_nodes(server_num)
        # self.graph = {
        #     0: [1, 4],
        #     1: [0, 2, 4],
        #     2: [1, 3],
        #     3: [2, 4, 5],
        #     4: [0, 1, 3],
        #     5: [3]
        # }

    def create_nodes(self, server_num):
        return {i: [] for i in range(server_num)}

    def add_edge(self, fr, to):
        self.graph[fr].append(to)
        self.graph[to].append(fr)

    def find_cliques(self):
        p = set(self.graph.keys())
        r = set()
        x = set()
        cliques = []
        for v in self.degeneracy_ordering():
            neighs = self.graph[v]
            self.find_cliques_pivot(r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
            p.remove(v)
            x.add(v)
        return sorted(cliques, key=lambda x: len(x))

    def find_cliques_pivot(self, r, p, x, cliques):
        if len(p) == 0 and len(x) == 0:
            cliques.append(r)
        else:
            u = iter(p.union(x)).__next__()
            for v in p.difference(self.graph[u]):
                neighs = self.graph[v]
                self.find_cliques_pivot(r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
                p.remove(v)
                x.add(v)

    def degeneracy_ordering(self):
        ordering = []
        ordering_set = set()
        degrees = defaultdict(lambda: 0)
        degen = defaultdict(list)
        max_deg = -1
        for v in self.graph:
            deg = len(self.graph[v])
            degen[deg].append(v)
            degrees[v] = deg
            if deg > max_deg:
                max_deg = deg

        while True:
            i = 0
            while i <= max_deg:
                if len(degen[i]) != 0:
                    break
                i += 1
            else:
                break
            v = degen[i].pop()
            ordering.append(v)
            ordering_set.add(v)
            for w in self.graph[v]:
                if w not in ordering_set:
                    deg = degrees[w]
                    degen[deg].remove(w)
                    if deg > 0:
                        degrees[w] -= 1
                        degen[deg - 1].append(w)

        ordering.reverse()
        return ordering


bk = BronKerbosch(5)
print(bk.find_cliques())
print(bk.find_cliques())

# bk = BronKerbosch(5)
# bk.add_edge(1, 2)
# bk.add_edge(1, 3)
# print(bk.graph)
