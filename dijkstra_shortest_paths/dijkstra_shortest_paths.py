import datetime

#read the input
class dijkstra_shortest_paths:
    def __init__(self, graph_file): #instantiate a graph every time class is called based on txt file
        self.graph = {} #attribute for graph
        self.edges = [] #attribute for graph edges alone
        with open(graph_file, 'r') as f: #assume input lists every vertex in first column, followed by tuples of head vertices forming an edge to the first column and their lengths
            lines = f.readlines()   #split lines in input for iteration
            for line in lines:
                items = line.split()    #split items (columns) on each line for iteration
                key = int(items[0])     #First column will be our graph key and tail for our list of edges
                values = []
                for item in items[1:]:  #iterate through all non-first column items
                    value = [int(i) for i in item.split(",")]   #convert each item in tuple to an integer
                    values.append(value)    #convert tuples to lists of integers
                    self.edges.append([key,value[0],value[1]])  #add edges to list of lists consisting of [tail, head, length]
                self.graph[key] = values

def dijkstra(self, s):  #shortest paths function, takes graph object and a starting vertex 's'
    X = {s}     #tracks vertices already explored
    self.paths = {}     #reset paths/answer to empty dictionary
    self.paths[s] = [0, []]     #set starting vertex s to length 0 and path empty
    for i in self.graph:    #for every other vertex, instantiate an entry in the dictionary with arbitrarily large/infinite length and empty path
        if i != s:
            self.paths[i] = [1000000,[]]
    while [edge for edge in self.edges if edge[0] in X and edge[1] not in X]:   #nested list comprehensions to check if any edges exist with on explored and one explored vertex
        vstartwstar = min([edge for edge in self.edges if edge[0] in X and edge[1] not in X], key=lambda x: self.paths[x[0]][0]+x[2]) #evaluate minimum edge where the total length of the path increases by the minimum amount to whatever the head vertex is
        X.add(vstartwstar[1])   #add the newly explored vertex to X
        self.paths[vstartwstar[1]][0] = self.paths[vstartwstar[0]][0]+vstartwstar[2]    #populate the answer with the newly identified distance/dijkstra score
        self.paths[vstartwstar[1]][1] = self.paths[vstartwstar[0]][1]+[vstartwstar[1]]  #populate the actual path to get to latest explored vertex (not necessary for core algorithm but useful in application
    return self.paths

if __name__ == '__main__':
    started = datetime.datetime.now()
    graph_object = dijkstra_shortest_paths('data.txt')
    print(dijkstra(graph_object,1))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)