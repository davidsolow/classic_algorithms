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
    median_sum = list[0]
    if list[0] < list[1]:
        h1.append(list[0])
        h2.append(list[1])
    else:
        h2.append(list[0])
        h1.append(list[1])
    median = h1[0]
    median_sum += median
    for i in list[2:200]:
        # print('Before--------------------')
        # print('Ordered?: ', h1[0] <= h2[0])
        # print('x: ', i)
        # print('h1 max: ', h1[0])
        # print('h1 real max: ', max(h1))
        # print('h2 min: ', h2[0])
        # print('h2 real min: ', min(h2))
        # print('h1 len: ', len(h1))
        # print('h2 len: ', len(h2))
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
        if len(h2) > len(h1):
            median = h2[0]
        else:
            median = h1[0]
        median_sum += median
        if h2[0] != min(h2):
            print('After--------------------')
            print('Ordered?: ', h1[0] <= h2[0])
            print('x: ', i)
            print('h1 max: ', h1[0])
            print('h1 real max: ', max(h1))
            print('h2 min: ', h2[0])
            print('h2 real min: ', min(h2))
            print('h1 len: ', len(h1))
            print('h2 len: ', len(h2))
            if i in h1:
                print('x put in h1')
            else: print('x put in h2')
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
    heap[0] = heap.pop()
    heap = bubble_down_max(heap, 0)
    return heap

def bubble_down_max(heap, position):
    left_child_position = position * 2 + 1
    right_child_position = position * 2 + 2
    if (left_child_position <= len(heap)-1 and right_child_position <= len(heap)-1) and (heap[position] < heap[left_child_position] or heap[position] < heap[right_child_position]):
        if heap[left_child_position] > heap[right_child_position]:
            heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
            position = left_child_position
        else:
            heap[position], heap[right_child_position] = heap[right_child_position], heap[position]
            position = right_child_position
        bubble_down_max(heap, position)
    elif left_child_position <= len(heap)-1 and heap[position] < heap[left_child_position]:
        heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
        position = left_child_position
        bubble_down_max(heap, position)
    return heap

# %% Helper function for extracting min from heap
def heap_extract_min(heap):
    heap[0] = heap.pop()
    heap = bubble_down_min(heap, 0)
    return heap

def bubble_down_min(heap, position):
    left_child_position = position * 2 + 1
    right_child_position = position * 2 + 2
    if (left_child_position <= len(heap)-1 and right_child_position <= len(heap)-1) and (heap[position] > heap[left_child_position] or heap[position] > heap[right_child_position]):
        if heap[left_child_position] < heap[right_child_position]:
            heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
            position = left_child_position
        else:
            heap[position], heap[right_child_position] = heap[right_child_position], heap[position]
            position = right_child_position
        bubble_down_min(heap, position)
    elif left_child_position <= len(heap)-1 and heap[position] > heap[left_child_position]:
        heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
        position = left_child_position
        bubble_down_min(heap, position)
    return heap

# %% codecell
if __name__ == '__main__':
    started = datetime.datetime.now()
    object = median_maintenance('median_maintenance_with_heaps/median_maintenance.txt').values
    tracksum_median(object)
    #print(tracksum_median(object))
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
