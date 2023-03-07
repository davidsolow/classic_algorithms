import datetime
import numpy as np
from itertools import combinations

class TSP:
    def __init__(self, data):
        self.graph = {}
        with open(data, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                items = line.split()
                self.graph[int(items[0])] = (float(items[1]), float(items[2]))
            self.n = len(self.graph)
        edges = list(combinations(range(1, self.n+1), 2))
        self.distances = {}
        for edge in edges:
            self.distances[(edge[0], edge[1])] = TSP.get_distance(self, edge[0], edge[1])
            
        self.solution = self.tsp()

    def get_distance(self, v, w):
        distance = np.sqrt((self.graph[v][0] - self.graph[w][0]) ** 2 + (self.graph[v][1] - self.graph[w][1]) ** 2)
        return distance
    
    def tsp(self):
        array = [[None for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                array[i][j] = TSP.get_distance(self, i+1, j+1)
        path = [0]
        start = 0
        cost = 0
        while len(path) < self.n:
            s = sorted([array[start][i] for i in range(self.n) if i not in path and i != start])
            shortest = s[0]
            next = array[start].index(shortest)
            path.append(next)
            start = next
            cost += shortest
        path.append(0)
        path = [i+1 for i in path]
        cost += array[next][0]
        return path, cost, array

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = TSP('data_big.txt')
    print(object.solution[0])
    print(object.solution[1])
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
