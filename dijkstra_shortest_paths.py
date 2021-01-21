import datetime

#read the input
class dijkstra_shortest_paths:
    def __init__(self, graph_file): #instantiate a graph every time class is called based on txt file
        self.graph = {} #attribute for graph
        self.edges = [] #attribute for graph edges alone
        with open(graph_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split()
                key = int(items[0])
                values = []
                for item in items[1:]:
                    value = [int(i) for i in item.split(",")]
                    values.append(value)
                    self.edges.append([key,value[0],value[1]])
                self.graph[key] = values

def dijkstra(self, s):
    X = {s}
    self.paths = {}
    self.paths[s] = [0, []]
    for i in self.graph:
        if i != s:
            self.paths[i] = [1000000,[]]
    while [edge for edge in self.edges if edge[0] in X and edge[1] not in X]:
        vstartwstar = min([edge for edge in self.edges if edge[0] in X and edge[1] not in X], key=lambda x: self.paths[x[0]][0]+x[2])
        X.add(vstartwstar[1])
        self.paths[vstartwstar[1]][0] = self.paths[vstartwstar[0]][0]+vstartwstar[2]
        self.paths[vstartwstar[1]][1] = self.paths[vstartwstar[0]][1]+[vstartwstar[1]]
    return self.paths

if __name__ == '__main__':
    started = datetime.datetime.now()
    graph_object = dijkstra_shortest_paths('data.txt')
    print(dijkstra(graph_object,1))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)