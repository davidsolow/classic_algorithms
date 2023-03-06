import datetime
import heapq
import sys
sys.setrecursionlimit(5000)

class Floyd:
    def __init__(self, data):
        self.graph = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            line_one = lines[0].split()
            self.v = int(line_one[0])
            self.e = int(line_one[1])
            for line in lines[1:]:
                items = line.split()
                self.graph[(int(items[0]), int(items[1]))] = int(items[2])
        self.shortest_path = self.floyd()

    def floyd(self):
        heap = []
        array = [[[None for k in range(self.v)] for w in range(self.v)] for v in range(self.v)]
        for v in range(self.v):
            for w in range(self.v):
                if v == w:
                    array[v][w][0] = 0
                elif (v+1,w+1) in self.graph.keys():
                    array[v][w][0] = self.graph[(v+1,w+1)]
                else:
                    array[v][w][0] = float('inf')
        for k in range(1, self.v):
            for v in range(self.v):
                for w in range(self.v):
                    array[v][w][k] = min(array[v][w][k-1], array[v][k][k-1] + array[k][w][k-1])
        for v in range(self.v):
            if array[v][v][self.v-1] < 0:
                return "Negative Cycle"
        for v in range(self.v):
            for w in range(self.v):
                heapq.heappush(heap, array[v][w][self.v-1])
        return heap[0]

if __name__ == '__main__':
    started = datetime.datetime.now()
    object1 = Floyd('data1.txt')
    object2 = Floyd('data2.txt')
    object3 = Floyd('data3.txt')
    print(object1.shortest_path)
    print(object2.shortest_path)
    print(object3.shortest_path)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)