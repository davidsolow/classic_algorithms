#Define class and get file into an adjacency list
class Kosaraju:
    def __init__(self, graph_file): #object instantiated based on a text file with one column of 'from' vertices and a second colume of 'to' vertices separated by new lines
        self.graph = {} #our normal graph
        self.graph_r = {}   #reversed graph for initial DFS search
        self.topoOrder = {}
        self.exploredTopo = []
        self.curLabel = len(self.graph)
        self.scc_number = 0
        self.scc = {}
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

#Kosaraju
def kosaraju(self):
    order = topo_sort(self)
    self.exploredTopo = []
    self.scc_number = 0
    self.scc = {}
    for v in sorted(order.items(), key=lambda x: x[1]):
        if v not in self.exploredTopo:
            self.scc_number += 1
            self.exploredTopo, self.scc = dfs_scc(self, v)
    return self.scc_number, self.scc

#Topological sort helper function to find order of reversed graph
def topo_sort(self):
    self.topoOrder = {}
    self.exploredTopo = []
    self.curLabel = len(self.graph)
    for v in self.graph_r:
        if v not in self.exploredTopo:
            self.exploredTopo, self.topoOrder, self.curLabel = dfs_topo(self, v)
    return self.topoOrder

#DFS Topo helper function to search graph and apply order numbers ie f(v) values
def dfs_topo(self, s):
    self.exploredTopo.append(s)
    for v in self.graph_r[s]:
        if v not in self.exploredTopo:
            dfs_topo(self, v)
    self.topoOrder[s] = self.curLabel
    self.curLabel -= 1
    return self.exploredTopo, self.topoOrder, self.curLabel

#DFS scc helper function to go through normal graph and accrue SCCs
def dfs_scc(self, s):
    self.exploredTopo.append(s)
    self.scc[s] = self.scc_number
    for v in self.graph[s]:
        if v not in self.exploredTopo:
            dfs_scc(self, v)
    return self.exploredTopo, self.scc

#Instantiate an object for data file and run Kosaraju on it
if __name__ == '__main__':
    graph_object = Kosaraju('test_data.txt')
    order1 = topo_sort(graph_object)
    print(sorted(order1.items(), key=lambda x: x[1]))