class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=' ')

        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)

print("Depth First Traversal (starting from node 1):")
g.dfs(1)