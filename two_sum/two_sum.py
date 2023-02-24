import datetime
class two_sum:
    def __init__(self, data, range_start, range_end):
        self.targets = {}
        self.values = set()
        for i in range(range_start, range_end+1):
            self.targets[i] = False
        with open(data, 'r') as f:
            for line in f:
                self.values.add(int(line))
        self.targets = two_sum.solve(self)
        self.number_of_two_sums = sum(1 for value in self.targets.values() if value)

    def two_sum(self, target):
        for x in self.values:
            y = target - x
            if y in self.values and y != x:
                return True
        return False
    
    def solve(self):
        for t in self.targets.keys():
            if two_sum.two_sum(self, t) == True:
                self.targets[t] = True
        return self.targets

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = two_sum('data.txt', -10000, 10000)
    print(object.number_of_two_sums)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)