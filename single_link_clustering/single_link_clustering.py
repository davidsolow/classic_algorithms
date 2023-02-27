import datetime
class SLC:
    def __init__(self, data, k = 4):
        self.graph = []
        self.k = k
        with open(data, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                items = line.split()
                items = [int(i) for i in items]
                self.graph.append(items)
        self.max_dist = SLC.slc(self)
    def slc(self):
        clusters = {}
        for e in self.graph:
            clusters[e[0]] = e[0]
            clusters[e[1]] = e[1]
        k = len(set(clusters.values()))
        max_dist = max([edge for edge in self.graph], key = lambda x: x[2])
        min_edge = min([edge for edge in self.graph if clusters[edge[0]] != clusters[edge[1]]], key = lambda x: x[2])
        print("Before:        ", clusters, min_edge, max_dist)
        while k > self.k:
            min_edge = min([edge for edge in self.graph if clusters[edge[0]] != clusters[edge[1]]], key = lambda x: x[2])
            clusters[min_edge[1]] = clusters[min_edge[0]]
            k = len(set(clusters.values()))
            max_dist = max([edge for edge in self.graph if clusters[edge[0]] == clusters[edge[1]]], key = lambda x: x[2])
            
            print("Iteration ", k, ": ", clusters, min_edge, max_dist)

        return clusters, max_dist

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = SLC('test.txt', k = 2)
    print(object.max_dist)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)

# Test answer: 5 for k = 2