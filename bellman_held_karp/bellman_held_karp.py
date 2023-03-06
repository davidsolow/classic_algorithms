import datetime

class BHK:
    def __init__(self, data):
        self.graph = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            line_one = lines[0].split()
            self.n = int(line_one[0])
            for i, line in enumerate(lines[1:], 1):
                a, b = map(float, line.split())
                self.graph[(i, int(a))] = b
        self.solution = self.bhk()

    def bhk(self):
        return self.graph

if __name__ == '__main__':
    started = datetime.datetime.now()
    bhk_object = BHK('test.txt')
    print(bhk_object.solution)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
