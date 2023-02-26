import datetime
class GreedyDiff:
    def __init__(self, data):
        self.jobs = []
        with open(data, 'r') as f:
            for line in f:
                items = line.split()
                sublist = [int(i) for i in items]
                self.jobs.append(sublist)
        self.jobs.pop(0)
        for i in self.jobs:
            ratio = i[0] / i[1]
            i.append(ratio)
        self.jobs = sorted(self.jobs, key = lambda x: (-x[2]))
        total = 0
        cum_len = 0
        for i in self.jobs:
            cum_len += i[1]
            weighted_len = i[0]*cum_len
            total += weighted_len
        self.total = total

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = GreedyDiff('data.txt')
    print(object.total)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)