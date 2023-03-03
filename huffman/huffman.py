import datetime
import math
import heapq

class Huffman:
    def __init__(self, data):
        forest = []
        with open(data, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                heapq.heappush(forest, int(line))
        print(forest)
        self.tree = self.huffman(forest)

    def huffman(self, forest):
        number_of_merges = 0
        while len(forest) >= 2:
            node1 = heapq.heappop(forest)
            node2 = heapq.heappop(forest)
            node3 = node1 + node2
            heapq.heappush(forest, node3)
            print(forest)
            break
            number_of_merges += 1
        return number_of_merges

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = Huffman('test.txt')
    print(object.tree)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)