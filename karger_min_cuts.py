import random
from random import randint

class Karger_Minimum_Cuts:
    def __init__(self, graph_file): #instantiate a graph every time class is called based on txt file
        self.v = {} #attribute for vertices
        self.e = 0  #attribute for total number of edges
        with open(graph_file) as file:
            for index, line in enumerate(file):
                numbers = [int(number) for number in line.split()]
                self.v[numbers[0]] = numbers[1:]
                self.e += len(numbers[1:])

    def random_edge(self):
        random_edge = randint(0, self.e - 1) #Random integer that will be used to reference all edges
        for vertex, edges in self.v.items():
            if len(edges) <= random_edge: #
                random_edge -= len(edges)
            else:
                from_vertex = vertex
                to_vertex = edges[random_edge]
                return from_vertex, to_vertex

    def find_min_cut(self):
        min_cut = 0
        while len(self.v) > 2:
            vertex_1, vertex_2 = self.random_edge()
            self.e -= len(self.v[vertex_1])
            self.e -= len(self.v[vertex_2])
            self.v[vertex_1].extend(self.v[vertex_2])
            for vertex in self.v[vertex_2]:
                self.v[vertex].remove(vertex_2)
                self.v[vertex].append(vertex_1)
            self.v[vertex_1] = list(filter(lambda v: v != vertex_1, self.v[vertex_1]))
            self.e += len(self.v[vertex_1])
            self.v.pop(vertex_2)
        for edges in self.v.values():
            min_cut = len(edges)
        return min_cut

if __name__ == '__main__':
    iterations = len(Karger_Minimum_Cuts('data.txt').v)
    minimum_cuts = iterations
    for i in range(iterations):
        cutter = Karger_Minimum_Cuts('data.txt')
        cut = cutter.find_min_cut()
        if cut < minimum_cuts:
            minimum_cuts = cut
    print(minimum_cuts)