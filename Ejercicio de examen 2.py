import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = {}

    def add_edge(self, src, dest, weight):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.vertices[src][dest] = weight
        self.vertices[dest][src] = weight

    def min_spanning_tree(self):
        edges = []
        for src in self.vertices:
            for dest, weight in self.vertices[src].items():
                if (weight, src, dest) not in edges and (weight, dest, src) not in edges:
                    edges.append((weight, src, dest))
        
        edges.sort()
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            root1, root2 = find(v1), find(v2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        mst = []
        for weight, src, dest in edges:
            if find(src) != find(dest):
                union(src, dest)
                mst.append((src, dest, weight))

        return mst

    def max_episode_shared(self):
        max_weight = 0
        pair = None
        for src in self.vertices:
            for dest, weight in self.vertices[src].items():
                if weight > max_weight:
                    max_weight = weight
                    pair = (src, dest)
        return pair, max_weight

    def contains_vertex(self, name):
        return name in self.vertices


g = Graph()


g.add_edge("Luke Skywalker", "Darth Vader", 4)
g.add_edge("Luke Skywalker", "Yoda", 2)
g.add_edge("Luke Skywalker", "Leia", 3)
g.add_edge("Leia", "Darth Vader", 1)
g.add_edge("Leia", "Han Solo", 3)
g.add_edge("Leia", "Chewbacca", 3)
g.add_edge("Leia", "C-3PO", 5)
g.add_edge("Chewbacca", "Han Solo", 4)
g.add_edge("Han Solo", "Rey", 2)
g.add_edge("Rey", "BB-8", 2)
g.add_edge("R2-D2", "Luke Skywalker", 3)
g.add_edge("Yoda", "R2-D2", 2)
g.add_edge("Darth Vader", "Kylo Ren", 1)


mst = g.min_spanning_tree()
contains_yoda = any("Yoda" in edge for edge in mst)


pair, max_shared_episodes = g.max_episode_shared()


print("Árbol de expansión mínimo:", mst)
print("El árbol contiene a Yoda:", contains_yoda)
print("Máximo de episodios compartidos entre dos personajes:", pair, "con", max_shared_episodes, "episodios")
