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
        counter = 0
        while counter <= 5: #len(forest) >= 2:
            t_one = forest.pop(forest.index(min(forest, key = sum)))
            t_two = forest.pop(forest.index(min(forest, key = sum)))
            t_three = Huffman.merge_trees(t_one, t_two)
            forest.append(t_three)
            counter += 1
        return forest
    
    def merge_trees(t_one, t_two):
        max_level = max(len(t_one) - 1, len(t_two) - 1, key = Huffman.get_level) + 1
        n_items = (2^(max_level)) - 1
        new_tree = [0] * n_items
        for i in range(max_level + 1):
            for j in t_one:
                if Huffman.get_level(t_one.index(j)) == i:
                    new_tree.append(j)
            for k in t_two:
                if Huffman.get_level(t_two.index(k)) == i:
                    new_tree.append(k)
        
        for i in range(1, len(new_tree)):
            for
            
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