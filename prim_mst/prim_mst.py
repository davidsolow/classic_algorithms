import datetime
class PrimMST:
    def __init__(self, data):
        self.graph = []
        with open(data, 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:
                items = line.split()
                items = [int(i) for i in items]
                self.graph.append(items)
        self.mst = PrimMST.prim(self, 1)

    def prim(self, s):
        x = {s}
        t = []
        while [edge for edge in self.graph if edge[0] in x and edge[1] not in x]:
            min_edge = min((edge for edge in self.graph if ((edge[0] in x and edge[1] not in x) or (edge[1] in x and edge[0] not in x)))
                           , key = lambda x: x[2])
            if min_edge[0] in x:
                x.add(min_edge[1])
            else:
                x.add(min_edge[0])
            t.append(min_edge)
        return t


if __name__ == '__main__':
    started = datetime.datetime.now()
    object = PrimMST('data.txt')
    print(sum(sub_list[2] for sub_list in object.mst))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)