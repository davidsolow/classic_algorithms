import random
from random import randint

class Karger_Minimum_Cuts:
    def __init__(self, graph_file): #instantiate a graph every time class is called based on txt file
        self.v = {} #attribute for vertices
        self.e = 0  #attribute for total number of edges
        with open(graph_file) as file:
            for index, line in enumerate(file):
                numbers = [int(number) for number in line.split()]
                self.v[numbers[0]] = numbers[1:] #Build adjacency list for each vertex/key in dictionary
                self.e += len(numbers[1:])  #store total number of edges

    def random_edge(self):
        random_edge = randint(0, self.e - 1) #Random integer that will be used to reference all edges
        for vertex, edges in self.v.items():
            if len(edges) <= random_edge: #if there are fewer edges then the random int that identifies a random edge, subtract the length of edges to prevent an error
                random_edge -= len(edges)
            else:   #Set edge as from the vertex/key and to the edge identified by the random int
                from_vertex = vertex
                to_vertex = edges[random_edge]
                return from_vertex, to_vertex

    def find_min_cut(self):
        min_cut = 0 #start at 0 each time funciton is called
        while len(self.v) > 2:  #keep collapsing edges until you get down to 2
            vertex_1, vertex_2 = self.random_edge() #pick a random edge to collapse
            self.e -= len(self.v[vertex_1]) #remove the edge
            self.e -= len(self.v[vertex_2]) #remove the edge (part 2)
            self.v[vertex_1].extend(self.v[vertex_2])
            for vertex in self.v[vertex_2]: #collapse the edge
                self.v[vertex].remove(vertex_2)
                self.v[vertex].append(vertex_1)
            self.v[vertex_1] = list(filter(lambda v: v != vertex_1, self.v[vertex_1]))  #remove any edges that point to/from to the same vertex after collapsing
            self.e += len(self.v[vertex_1]) #update total number of edges
            self.v.pop(vertex_2)
        for edges in self.v.values():   #count number of edges in min cut after all collapsing is done
            min_cut = len(edges)
        return min_cut

if __name__ == '__main__':
    iterations = len(Karger_Minimum_Cuts('data.txt').v) #set number of times min cuts will be run to increase probability to something acceptable
    minimum_cuts = iterations
    for i in range(iterations):
        cutter = Karger_Minimum_Cuts('data.txt')
        cut = cutter.find_min_cut()
        if cut < minimum_cuts:  #keep replacing min cuts variable each time you find a smaller result
            minimum_cuts = cut
    print(minimum_cuts)