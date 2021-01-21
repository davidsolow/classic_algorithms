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
    graph_object = dijkstra_shortest_paths('test_data.txt')
    print(graph_object.graph)
    print(graph_object.edges)
    print(dijkstra(graph_object,1))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)

##TEST CASES ------------------------------------------------------------------------------------------------
#Test 1: Input reads correctly
input = {1: [[2,1], [8,2]],
         2: [[1,1], [3,1]],
         3: [[2,1], [4,1]],
         4: [[3,1], [5,1]],
         5: [[4,1], [6,1]],
         6: [[5,1], [7,1]],
         7: [[6,1], [8,1]],
         8: [[7,1], [1,2]]}
print(str(input) == str(graph_object.graph))

#Test 2: Output shortest paths (both length and actual path) for each vertex in graph
answer = {1: [0, []],
          2: [1, [2]],
          3: [2, [2,3]],
          4: [3, [2,3,4]],
          5: [4, [2,3,4,5]],
          6: [4, [8,7,6]],
          7: [3, [8,7]],
          8: [2, [8]]}
print(str(answer) == str(dijkstra(graph_object, 1)))