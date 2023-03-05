import datetime

class Knapsack:
    def __init__(self, data):
        self.items = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            line_one = lines[0].split()
            self.capacity = int(line_one[0])
            self.n = int(line_one[1])
            for line in enumerate(lines[1:]):
                item = line[1].split()
                self.items[line[0]+1] = [int(item[0]), int(item[1])]
        self.solution = self.knapsack()

    def knapsack(self):
        array = [[None for j in range(self.n + 1)] for i in range(self.capacity + 1)]
        for c in range(self.capacity + 1):
            array[c][0] = 0
        for i in range(1, self.n + 1):
            size_i = self.items[i][1]
            value_i = self.items[i][0]
            for c in range(self.capacity + 1):
                if size_i > c:
                    array[c][i] = array[c][i-1]
                else:
                    array[c][i] = max(array[c][i-1], array[c - size_i][i-1] + value_i)
        return array[self.capacity][self.n]

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = Knapsack('data.txt')
    print(object.solution)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)