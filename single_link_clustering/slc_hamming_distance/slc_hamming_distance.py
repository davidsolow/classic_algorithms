import datetime

class SLC:
    def __init__(self, data, n):
        self.raw_graph = {}
        self.max_space = 3 # Hardcoding this for given problem/data
        with open(data, 'r') as f:
            lines = f.readlines()
            self.n = n
            for i, line in enumerate(lines[1:], 1):
                items = line.split()
                items = [int(i) for i in items]
                self.raw_graph[tuple(items)] = i
        self.graph = []
        for i in self.raw_graph.keys():
            node = list(i)
            for j in range(len(node)):
                node_t = node.copy()
                node_t[j] ^= 1
                if tuple(node_t) in self.raw_graph:
                    self.graph.append([self.raw_graph[i], self.raw_graph[tuple(node_t)], 1])
            for j in range(len(node)):
                for k in range(j + 1, len(node)):
                    node_t = node.copy()
                    node_t[j] ^= 1
                    node_t[k] ^= 1
                    if tuple(node_t) in self.raw_graph:
                        self.graph.append([self.raw_graph[i], self.raw_graph[tuple(node_t)], 2])          
        self.max_k = self.slc()

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def slc(self):
        t = set()
        graph = sorted(self.graph, key=lambda x: x[2])
        parent = [i for i in range(self.n+1)]
        rank = [0 for i in range(self.n+1)]
        count = self.n
        for edge in graph:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            if x != y:
                t.add(tuple(edge))
                self.union(parent, rank, x, y)
                count -= 1
        return count

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = SLC('data.txt', 200000)
    print(object.max_k)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)