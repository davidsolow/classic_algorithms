import datetime
class median_maintenance:
    # Initiate class with just a list of values to read
    def __init__(self, values_file):
        self.values = []
        with open(values_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split()
                self.values.append(int(items[0]))

    """
    tracksum:
    Sums the medians in a set of values as additional values are read. Works only for set of unique integers.

    Args:
        self = class object
    """

    def tracksum_median(self):
        h1 = []
        h2 = []
        median_sum = 0
        if self.values[0] <= self.values[1]:
            h1.append(self.values[0])
            h2.append(self.values[1])
        else:
            h2.append(self.values[0])
            h1.append(self.values[1])
        median = h2[0]
        median_sum += median
        for i in self.values[2:]:
            if i <= h1[0]:
                h1 = heap_insert_max(h1, i)
            else:
                h2 = heap_insert_min(h2, i)
            if len(h1) - len(h2) > 1:
                h2 = heap_insert_min(h2, h1[0])
                h1 = heap_extract(h1)
            elif len(h2) - len(hq) > 1:
                h1 = heap_insert_max(h1, h2[0])
                h2 = heap_extract(h2)
            else: pass
            median = h1[0]
            median_sum += median
        return median_sum

    # Helper function to insert for heap built for extracting maximumus
    def heap_insert_max(heap, value):
        heap.append(value)
        child = len(heap)-1
        parent = child // 2
        while heap[parent] < heap[child] and child != 0:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = child // 2
            parent = parent // 2
        return heap

    # Helpter function to insert for heap built for extraming minimums
    def heap_insert_min(heap, value):
        heap.append(value)
        child = len(heap)-1
        parent = child // 2
        while heap[parent] > heap[child] and child != 0:
            heap[parent], heap[child] = heap[child], heap[parent]
            child = child // 2
            parent = parent // 2
        return heap
    # Helper function for extracting min/max from heap
    def heap_extract(heap):
        return

if __name__ == '__main__':
    started = datetime.datetime.now()
    #object = median_maintenance('median_maintenance_with_heaps/median_maintenance.txt')
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
