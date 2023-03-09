import datetime
from collections import Counter, defaultdict
import threading

threading.stack_size(67108864)

class Papa:
    def __init__(self, data):
        with open(data) as f:
            lines = f.readlines()
            self.clauses = {(int(items[0]), int(items[1])) for items in [line.split() for line in lines[1:]]}
        clause_vals = set()
        for first, second in self.clauses:
            clause_vals.add(first)
            clause_vals.add(second)
        self.clauses = {tup for tup in self.clauses if all(-val in clause_vals for val in tup)}
        counts = Counter(abs(val) for tup in self.clauses for val in tup)
        while min(counts.values()) < 2:
            self.clauses = {tup for tup in self.clauses if all(-val in clause_vals for val in tup)}
            self.clauses = {tup for tup in self.clauses if all(counts[abs(val)] > 1 for val in tup)}
            counts = Counter(abs(val) for tup in self.clauses for val in tup)
        self.value_counts = defaultdict(int)
        for first, second in self.clauses:
            self.value_counts[first] += 1
            self.value_counts[second] += 1
        self.values = {abs(i): True for tup in self.clauses for i in tup}
        for first, second in self.clauses:
            if first < 0:
                self.values[first] = False
            if second < 0:
                self.values[second] = False
        self.n = len(self.values.keys())
        self.solution = self.papa()
    
    def papa(self):
        for i in range(round(2*(self.n**2))):
            all_satisfied = True
            for first, second in self.clauses:
                if (first > 0) ^ self.values[abs(first)] and (second > 0) ^ self.values[abs(second)]:
                    all_satisfied = False
                    if self.value_counts[first] > self.value_counts[second]:
                        self.values[abs(first)] ^= True
                    else:
                        self.values[abs(second)] ^= True
                    break
            if all_satisfied:
                return "Satisfiable"
        return "Not Satisfiable"

if __name__ == "__main__":
    def main():
        started = datetime.datetime.now()
        obj = Papa('data1.txt')
        print(obj.solution)
        ended = datetime.datetime.now()
        runtime = ended - started
        print("Runtime: ", runtime)

    thread = threading.Thread(target=main)
    thread.start()
