#Import libraries
import sys, threading, datetime
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

#Define class and get file into an adjacency list
class Kosaraju:
    def __init__(self, graph_file, number_of_vertices): #object instantiated based on a text file with one column of 'from' vertices and a second colume of 'to' vertices separated by new lines
        self.graph = {} #our normal graph
        self.graph_r = {}   #reversed graph for initial DFS search
        self.topoOrder = {}
        for i in range(1, number_of_vertices+1):
            self.topoOrder[i] = 0
        self.number_of_vertices = number_of_vertices
        self.exploredTopo = {}
        for i in range(1, number_of_vertices+1):
            self.exploredTopo[i] = False
        self.curLabel = number_of_vertices
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
        for i in range(1,number_of_vertices+1):
            if i not in self.graph.keys():
                self.graph[i] = []
            if i not in self.graph_r.keys():
                self.graph_r[i] = []

#Kosaraju
def kosaraju_scc(self):
    order = topo_sort(self)
    self.exploredTopo = dict.fromkeys(self.exploredTopo, False)
    self.scc_number = 0
    self.scc = {}
    for v in order.values():
        if self.exploredTopo[v] == False:
            self.scc_number += 1
            self.exploredTopo, self.scc = dfs_scc(self, v)
    scc_list = list(set(self.scc.values()))
    top5 = {}
    for i in scc_list:
        top5[i] = 0
    while len(top5) < 5:
        top5[len(top5)+1] = 0
    for j in self.scc.values():
        top5[j] += 1
    top5 = {k: v for k, v in sorted(top5.items(), key=lambda item: item[1])}
    top5 = list(top5.values())
    top5 = [top5[-1], top5[-2], top5[-3], top5[-4], top5[-5]]
    return top5

#Topological sort helper function to find order of reversed graph
def topo_sort(self):
    self.topoOrder = dict.fromkeys(self.topoOrder, 0)
    self.exploredTopo = dict.fromkeys(self.exploredTopo, False)
    self.curLabel = self.number_of_vertices
    for v in self.graph_r:
        if self.exploredTopo[v] == False:
            self.exploredTopo, self.topoOrder, self.curLabel = dfs_topo(self, v)
    return self.topoOrder

#DFS Topo helper function to search graph and apply order numbers ie f(v) values
def dfs_topo(self, s):
    self.exploredTopo[s] = True
    for v in self.graph_r[s]:
        if self.exploredTopo[v] == False:
            dfs_topo(self, v)
    self.topoOrder[self.curLabel] = s
    self.curLabel -= 1
    return self.exploredTopo, self.topoOrder, self.curLabel

#DFS scc helper function to go through normal graph and accrue SCCs
def dfs_scc(self, s):
    self.exploredTopo[s] = True
    self.scc[s] = self.scc_number
    for v in self.graph[s]:
        if self.exploredTopo[v] == False:
            dfs_scc(self, v)
    return self.exploredTopo, self.scc

#Instantiate an object for data file and run Kosaraju on it
def main():
    if __name__ == '__main__':
        started = datetime.datetime.now()
        graph_object = Kosaraju('data.txt', 875714)
        print(kosaraju_scc(graph_object))
        ended = datetime.datetime.now()
        runtime = ended - started
        print("Runtime: ", runtime)
thread = threading.Thread(target=main)
thread.start()