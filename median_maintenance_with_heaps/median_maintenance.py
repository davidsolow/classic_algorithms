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

def tracksum_median(list):
    h1 = []
    h2 = []
    median_sum = 0
    if list[0] < list[1]:
        h1.append(list[0])
        h2.append(list[1])
    else:
        h2.append(list[0])
        h1.append(list[1])
    median = h1[0]
    median_sum += median
    for i in list[2:]:
        if i < h2[0]:
            h1 = heap_insert_max(h1, i)
        else:
            h2 = heap_insert_min(h2, i)
        if len(h1) - len(h2) > 1:
            h2 = heap_insert_min(h2, h1[0])
            h1 = heap_extract_max(h1)
        elif len(h2) - len(h1) > 1:
            h1 = heap_insert_max(h1, h2[0])
            h2 = heap_extract_min(h2)
        median = h1[0]
        median_sum += median
        #print(len(h1)-len(h2))
        print(list.index(i), i, h1[0], h2[0], h1[0] <= h2[0])
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

# Helper function to insert for heap built for extraming minimums
def heap_insert_min(heap, value):
    heap.append(value)
    child = len(heap)-1
    parent = child // 2
    while heap[parent] > heap[child] and child != 0:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = child // 2
        parent = parent // 2
    return heap

# Helper function for extracting max from heap
def heap_extract_max(heap):
    position = 0
    heap[position] = heap.pop()
    left_child = position * 2 + 1
    right_child = position * 2 + 2
    while (left_child <= len(heap)-1 and right_child <= len(heap)-1) and (heap[position] < heap[left_child] or heap[position] < heap[right_child]):
            if heap[left_child] > heap[right_child]:
                largest = left_child
            else:
                largest = right_child
            heap[position], heap[largest] = heap[largest], heap[position]
            position = largest
            left_child = position * 2 + 1
            right_child = position * 2 + 2
    if left_child <= len(heap)-1:
        if heap[left_child] > heap[position]:
            heap[position], heap[left_child] = heap[left_child], heap[position]
    return heap

# Helper function for extracting min from heap
def heap_extract_min(heap):
    position = 0
    heap[position] = heap.pop()
    left_child = position * 2 + 1
    right_child = position * 2 + 2
    while (left_child <= len(heap)-1 and right_child <= len(heap)-1) and (heap[position] > heap[left_child] or heap[position] > heap[right_child]):
            if heap[left_child] < heap[right_child]:
                smallest = left_child
            else:
                smallest = right_child
            heap[position], heap[smallest] = heap[smallest], heap[position]
            position = smallest
            left_child = position * 2 + 1
            right_child = position * 2 + 2
    if left_child <= len(heap)-1:
        if heap[left_child] < heap[position]:
            heap[position], heap[left_child] = heap[left_child], heap[position]
    return heap

if __name__ == '__main__':
    started = datetime.datetime.now()
    object = median_maintenance('median_maintenance_with_heaps/median_maintenance.txt').values
    print(tracksum_median(object))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
