#Define class and get file into an adjacency list
class Kosaraju:
    def __init__(self, graph_file): #object instantiated based on a text file with one column of 'from' vertices and a second colume of 'to' vertices separated by new lines
        self.graph = {} #our normal graph
        self.graph_r = {}   #reversed graph for initial DFS search
        with open(graph_file) as file:
            for index, line in enumerate(file):
                key = int(line.split()[0])  #dictionary key for adjacency list (from vertex is always a key)
                value = int(line.split()[1])    #dictionary value for adjacency list (to vertices are always values)
                if key not in self.graph:
                    self.graph[key] = [value]   #make first entry a list
                else:
                    self.graph[key].append(value)   #append all other entries to key
                if value not in self.graph_r:   #do the opposite for the reverse graph
                    self.graph_r[value] = [key]
                else:
                    self.graph_r[value].append(key)

#DFS Topo helper function to search graph and apply order numbers ie f(v) values
def dfs_topo(self, s, exploredTopo, curLabel, topoOrder):
    exploredTopo.append(s)
    for v in self.graph_r[s]:
        if v not in exploredTopo:
            dfs_topo(self, v, exploredTopo, curLabel, topoOrder)
    topoOrder[s] = curLabel
    curLabel -= 1
    return exploredTopo, curLabel, topoOrder

#Topological sort helper function to find order of reversed graph
def topo_sort(self):
    topoOrder = {}
    exploredTopo = []
    curLabel = len(self.graph_r)
    for v in self.graph_r:
        if v not in exploredTopo:
            exploredTopo += dfs_topo(self, v, exploredTopo, curLabel, topoOrder)[0]
            topoOrder.udpate(dfs_topo(self, v, exploredTopo, curLabel, topoOrder)[2])
            curLabel = dfs_topo(self, v, exploredTopo, curLabel, topoOrder)[1]
    return topoOrder

#Depth-First-Search with SCC label Helper Function


#Instantiate an object for data file and run Kosaraju on it
graph_object = Kosaraju('data.txt')
print(topo_sort(graph_object))