import datetime

class SLC:
    def __init__(self, data, n, k=4):
        self.graph = []
        self.k = k
        with open(data, 'r') as f:
            lines = f.readlines()
            self.n = n
            for line in lines[1:]:
                items = line.split()
                items = [int(i) for i in items]
                self.graph.append(items)
        self.max_dist = self.slc()

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
        t = []
        graph = sorted(self.graph, key=lambda x: x[2])
        parent = [i for i in range(self.n+1)]
        rank = [0 for i in range(self.n+1)]
        count = self.n
        for edge in graph:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            if x != y:
                t.append(edge)
                self.union(parent, rank, x, y)
                count -= 1
                if count == self.k:
                    break

        max_spacing = float('inf')
        for edge in graph:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            if x != y and edge[2] < max_spacing:
                max_spacing = edge[2]
        return max_spacing

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = SLC('data.txt', n = 500, k=4)
    print(object.max_dist)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)