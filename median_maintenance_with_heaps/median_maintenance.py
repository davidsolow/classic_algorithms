import datetime
class median_maintenance:
    """
    Maintains the median in a set of values as additional values are added.

    Args:
        values_file = a list of integers
    """

    # Just initiate a list of all values
    def __init__(self, values_file):
        self.values = []
        with open(values_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split()
                self.values.append(int(items[0]))
    # define insert for h1 with findmax
    def insert_h1(heap, value):
        heap.append(value)
        if

    # define insert for h2 with findmin

    # Place starting root notes of heaps 1 and 2
    def tracksum_median(self.values)
        self.h1 = []
            self.h2 = []
            if self.values[0] <= self.values[1]:
                self.h1.append(self.values[0])
                self.h2.append(self.values[1])
            else:
                self.h2.append(self.values[0])
                self.h1.append(self.values[1])

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = median_maintenance('median_maintenance_with_heaps/median_maintenance.txt')
    print(object.h1)
    print(object.h2)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
