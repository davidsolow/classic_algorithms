import datetime

class Floyd:
    def __init__(self, data):
        self.graph = {}
        self.cache = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            line_one = lines[0].split()
            self.v = int(line_one[0])
            self.e = int(line_one[1])
            for line in lines[1:]:
                items = line.split()
                self.graph[(int(items[0]), int(items[1]))] = int(items[2])
        self.shortest_path = self.floyd(v=self.v, w=self.v, k=self.v)
        self.is_negative_cycle = self.cycle_check()

    def floyd(self, v, w, k):
        if k == 1:
            if v == w:
                solution = 0
                self.cache[(v,w,k)] = solution
                return solution
            elif (v,w) in self.graph.keys():
                solution = self.graph[(v,w)]
                self.cache[(v,w,k)] = solution
                return solution
            else:
                return float('inf')
        if (v,w,k) in self.cache.keys():
            return self.cache[(v,w,k)]
        solution = min(Floyd.floyd(self, v=v, w=w, k=k-1), Floyd.floyd(self, v=v, w=k, k=k-1) + Floyd.floyd(self, v=k, w=w, k=k-1))
        self.cache[(v,w,k)] = solution
        return solution
    
    def cycle_check(self):
        for v in range(1, self.v+1):
            print(v)
            if self.cache[(v,v,self.v)] < 0:
                return "Negative_Cycle"

if __name__ == '__main__':
    started = datetime.datetime.now()
    object1 = Floyd('test.txt')
    #object2 = Floyd('data2.txt')
    #object3 = Floyd('data3.txt')
    print(min(object1.cache.values()))
    print(object1.is_negative_cycle)
    #print(object2.shortest_path)
    #print(object3.shortest_path)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)