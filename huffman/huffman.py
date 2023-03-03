import datetime
import math

class Huffman:
    def __init__(self, data):
        forest = []
        with open(data, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                item = line.split()
                item = [int(i) for i in item]
                forest.append(item)
        self.tree = self.huffman(forest)

    def huffman(self, forest):
        while len(forest) >= 2:
            t_one = forest.pop(forest.index(min(forest, key = sum)))
            t_two = forest.pop(forest.index(min(forest, key = sum)))
            t_three = Huffman.merge_trees(t_one, t_two)
            forest.append(t_three)
        return forest
    
    def merge_trees(t_one, t_two):
        new_tree = [0]
        max_level = max(len(t_one) - 1, len(t_two) - 1, key = Huffman.get_level)
        for i in range(max_level + 1):
            for j in t_one:
                if Huffman.get_level(t_one.index(j)) == i:
                    new_tree.append(j)
            for k in t_two:
                if Huffman.get_level(t_two.index(k)) == i:
                    new_tree.append(k)
        return new_tree

    def get_level(index):
        return math.floor(math.log2(index + 1))

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = Huffman('test.txt')
    print(object.tree)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)