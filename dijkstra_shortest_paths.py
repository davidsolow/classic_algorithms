#read the input
class dijkstra_shortest_paths:
    def __init__(self, graph_file): #instantiate a graph every time class is called based on txt file
        self.graph = {} #attribute for graph
        with open(graph_file) as file:
            for index, line in enumerate(file):
                items = [item for item in line.split()]
                key = int(items[0])
                #for i in range(1,len(items)):
                    #items[i] = [int(j) for j in items[i][0]]
                self.graph[key] = [value for value in items[1:]]

graph_object = dijkstra_shortest_paths('test_data.txt')
print(graph_object.graph)

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
          4: [2, [2,3,4]],
          5: [4, [2,3,4,5]],
          6: [4, [8,7,6]],
          7: [3, [8,7]],
          8: [2, [8]]}