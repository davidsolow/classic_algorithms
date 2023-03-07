import datetime
import numpy as np
from itertools import combinations

class TSP:
    def __init__(self, data):
        with open(data, 'r') as f:
            lines = f.readlines()[1:]
            self.graph = [list(map(float, i.split(' '))) for i in lines]
            self.n = len(self.graph)
        edges = list(combinations(range(1, self.n+1), 2))
        self.distances = {}
        for edge in edges:
            self.distances[(edge[0], edge[1])] = TSP.get_distance(self, edge[0]-1, edge[1]-1)
            
        self.solution = self.tsp()

    def get_distance(self, v, w):
        distance = np.sqrt((self.graph[v][0] - self.graph[w][0]) ** 2 + (self.graph[v][1] - self.graph[w][1]) ** 2)
        return distance
    
    def tsp(self):
        previous = {(0): {0: 0}}
        for m in range(1, self.n):
            combs = list(combinations(range(1, self.n), m))
            current = {(combs[i]): {list(combs[i])[j]: 0 for j in range(m)} for i in range(len(combs))}
            for S in current:
                for j in S:
                    if m == 1:
                        current[S][j] = TSP.get_distance(self, 0, j)
                    else:
                        ij = (S)
                        ij = tuple(x for x in ij if x != j)
                        current[S][j] = min([previous[(ij)][k] + TSP.get_distance(self, k, j) for k in ij if k != j])
            previous = current.copy()
        return min([current[(combs[0])][j] + TSP.get_distance(self, 0, j) for j in range(1, self.n)])

if __name__ == '__main__':
    started = datetime.datetime.now()
    bhk_object = TSP('data.txt')
    print(bhk_object.solution)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
