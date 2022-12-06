class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
def search_graph(parent, i):
    if parent[i] == i:
        return i
    return search_graph(parent, parent[i])

  
def kruskal(self):
    result = []
    i, e = 0, 0
    self.graph = sorted(self.graph, key=lambda item: item[2])
    parent = []
    pound = []
    for node in range(self.V):
        parent.append(node)
        pound.append(0)
    while e < self.V - 1:
        u, v, w = self.graph[i]
        i = i + 1
        x = search_graph(parent, u)
        y = search_graph(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            a_root = search_graph(parent, x)
            b_root = search_graph(parent, y)
            if pound[a_root] < pound[b_root]:
                parent[a_root] = b_root
            elif pound[a_root] > pound[b_root]:
                parent[b_root] = a_root
            else:
                parent[b_root] = a_root
                pound[a_root] += 1


    for u, v, weight in result:
        print(f"Edge:{u} {v} - {weight}")
 
graph1= Graph(5)
graph1.add_edge(0, 1, 8)
graph1.add_edge(1, 2, 9)
graph1.add_edge(1, 3, 11)
graph1.add_edge(2, 3, 15)
graph1.add_edge(2, 4, 10)
graph1.add_edge(3, 4, 7)
kruskal(graph1)
