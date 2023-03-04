import datetime
import math
import heapq

class Huffman:
    def __init__(self, data):
        forest = []
        tracker = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                forest.append((int(line), [int(line)]))
                tracker[int(line)] = 0
        heapq.heapify(forest)
        self.tree = self.huffman(forest, tracker)

    def huffman(self, forest, tracker):
        while len(forest) >= 2:
            node1 = heapq.heappop(forest)
            node2 = heapq.heappop(forest)
            node3 = (node1[0] + node2[0], node1[1] + node2[1])
            heapq.heappush(forest, node3)
            for i in node3[1]:
                tracker[i] = tracker[i] + 1
        return forest, tracker, max(tracker.values()), min(tracker.values())

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = Huffman('data.txt')
    print(object.tree[2:])
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)