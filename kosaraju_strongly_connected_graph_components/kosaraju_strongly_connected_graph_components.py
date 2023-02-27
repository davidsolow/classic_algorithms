#Import libraries
import sys, threading, datetime
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

#Define class and get file into an adjacency list
class Kosaraju:
    def __init__(self, graph_file, number_of_vertices): #object instantiated based on a text file with one column of 'from' vertices and a second colume of 'to' vertices separated by new lines
        self.graph = {} #our normal graph
        self.graph_r = {}   #reversed graph for initial DFS search
        self.topoOrder = {} #will store topographical order of reversed graph later used to identify SCCs in normal graph
        for i in range(1, number_of_vertices+1):    #Instantiate each vertex's topo order as 0
            self.topoOrder[i] = 0
        self.number_of_vertices = number_of_vertices    #store number of vertices so that functions can be re-run on same object
        self.exploredTopo = {}  #stores booleans for whether or not each vertex has been explored during depth first search routines
        for i in range(1, number_of_vertices+1):    #instantiate each vertex's explored status as False/unexplored
            self.exploredTopo[i] = False
        self.curLabel = number_of_vertices  #separate variable to store topological oder, start with last order number ie number of vertices
        self.scc_number = 0 #identifier for SCCs, start with 0
        self.scc = {} #Intantiate dictionary that will contain each vertex and its associated SCC
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
        for i in range(1,number_of_vertices+1): #Edge case - assign an empty list in the case that any vertex key doesn't have any edges (prevents key errors)
            if i not in self.graph.keys():
                self.graph[i] = []
            if i not in self.graph_r.keys():
                self.graph_r[i] = []

#Kosaraju
def kosaraju_scc(self):
    order = topo_sort(self) #confirm order by which SCCs can be identified via DFS on normal graph by getting topo order of reverse graph
    self.exploredTopo = dict.fromkeys(self.exploredTopo, False) #mark every vertex as unexplored to make sure function works cleanly each time its called
    self.scc_number = 0 #start SCC tracker back at 0 each time function is called
    self.scc = {}   #start SCC dictionary back at empty each time function is called
    for v in order.values():    #in the reverse topological order, search through unexplored vertices using DFS, anytime you can't reach the next vertex in a DFS call you've reached the end of an SCC
        if self.exploredTopo[v] == False:
            self.scc_number += 1
            self.exploredTopo, self.scc = dfs_scc(self, v)
    scc_list = list(set(self.scc.values())) #In this case, we'll output the top 5 largest SCCs - this list stored unique SCCs to help
    top5 = {}   #empty dictionary that will eventually be our 5 largest SCCs
    for i in scc_list:  #instantiate each SCC size as 0
        top5[i] = 0
    while len(top5) < 5:    #Edge case - if there are less than 5 SCCs, put some placeholders in and make them 0
        top5[len(top5)+1] = 0
    for j in self.scc.values(): #Increment number of vertices in each SCC each time you encounter the same SCC number
        top5[j] += 1
    top5 = {k: v for k, v in sorted(top5.items(), key=lambda item: item[1])}    #Sort SCCs by number of vertices increasing
    top5 = list(top5.values())  #convert values to list of just vertex counts
    top5 = [top5[-1], top5[-2], top5[-3], top5[-4], top5[-5]]   #subset top 5 in decreasing order
    return top5

#Topological sort helper function to find order of reversed graph
def topo_sort(self):
    self.topoOrder = dict.fromkeys(self.topoOrder, 0)   #Set all topo orders to 0 to start
    self.exploredTopo = dict.fromkeys(self.exploredTopo, False) #Set all vertices to unexplored to start
    self.curLabel = self.number_of_vertices #reset topo order tracker to end point ie total number of vertices
    for v in self.graph_r:  #Call depth first search for every unexplored vertex
        if self.exploredTopo[v] == False:
            self.exploredTopo, self.topoOrder, self.curLabel = dfs_topo(self, v)
    return self.topoOrder

#DFS Topo helper function to search graph and apply order numbers ie f(v) values
def dfs_topo(self, s):
    self.exploredTopo[s] = True #Mark the vertex that DFS is being called on as explored
    for v in self.graph_r[s]:   #recursively call DFS on all vertices adjacent to the vertex passed to DFS (if unexplored)
        if self.exploredTopo[v] == False:
            dfs_topo(self, v)
    self.topoOrder[self.curLabel] = s   #Assign topo order to vertex
    self.curLabel -= 1  #decrement topo order tracker each time an order is assigned
    return self.exploredTopo, self.topoOrder, self.curLabel #pass back all relevant attributes for later DFS calls

#DFS scc helper function to go through normal graph and accrue SCCs
def dfs_scc(self, s):
    self.exploredTopo[s] = True #mark vertex being called in DFS as explored
    self.scc[s] = self.scc_number   #Assign current SCC number to vertex being called
    for v in self.graph[s]: #recursively call DFS for all vertices adjacent to the vertex passed to DFS (if unexplored)
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
thread = threading.Thread(target=main)  #Since this algorithm relies on recursion and since base Python is not good with stack sizes/memory, use threading to back-door smaller stack sizes
thread.start()
