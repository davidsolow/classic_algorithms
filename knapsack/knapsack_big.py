import datetime
import sys
sys.setrecursionlimit(5000)

class Knapsack:
    def __init__(self, data):
        self.items = {}
        self.cache = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            line_one = lines[0].split()
            self.capacity = int(line_one[0])
            self.n = int(line_one[1])
            for line in enumerate(lines[1:]):
                item = line[1].split()
                self.items[line[0]+1] = [int(item[0]), int(item[1])]
        self.solution = self.knapsack(self.n, self.capacity)

    def knapsack(self, i, c):
        if i == 1:
            return 0
        size_i = self.items[i][1]
        value_i = self.items[i][0]
        if (i,c) in self.cache.keys():
            return self.cache[(i,c)]
        if size_i > c:
            solution = Knapsack.knapsack(self, i-1, c)
            self.cache[(i,c)] = solution
            return solution
        else:
            solution = max(Knapsack.knapsack(self, i-1, c), Knapsack.knapsack(self, i-1, c - size_i) + value_i)
            self.cache[(i,c)] = solution
            return solution

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = Knapsack('data_big.txt')
    print(object.solution)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)