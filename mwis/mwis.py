import datetime

class MWIS:
    def __init__(self, data):
        self.weights = {}
        with open(data, 'r') as f:
            lines = f.readlines()
            self.n = int(lines[0])
            for line in enumerate(lines[1:]):
                self.weights[line[0]+1] = int(line[1])              
        self.mwis = self.mwis()
        self.s = self.reconstruct()
            
    def mwis(self):
        v = [0]
        v.append(self.weights[1])
        for i in range(2, self.n + 1):
            v.append(max(v[i-1], v[i-2] + self.weights[i]))
        return v
    
    def reconstruct(self):
        s = set()
        i = self.n
        while i >= 2:
            if self.mwis[i-1] >= self.mwis[i-2] + self.weights[i]:
                i -= 1
            else:
                s.add(i)
                i -= 2
        if i == 1:
            s.add(1)
        return s

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = MWIS('data.txt')
    print(object.mwis[-1])
    vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    answer = ""
    for i in vertices:
        if i in object.s:
            answer += "1"
        else:
            answer += "0"
    print(answer)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)