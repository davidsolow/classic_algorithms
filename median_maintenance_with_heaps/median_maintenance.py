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
        self.median_sum = median_maintenance.tracksum_median(self.values)

    """
    tracksum:
    Sums the medians in a set of values as additional values are read. Works only for set of unique integers.

    Args:
        list = list of integers compiled from class instantiation
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
        num_medians = 2
        for i in list[2:]:
            if i < h2[0]:
                h1 = median_maintenance.heap_insert_max(h1, i)
            else:
                h2 = median_maintenance.heap_insert_min(h2, i)
            if len(h1) - len(h2) > 1:
                h2 = median_maintenance.heap_insert_min(h2, h1[0])
                h1 = median_maintenance.heap_extract_max(h1)
            elif len(h2) - len(h1) > 1:
                h1 = median_maintenance.heap_insert_max(h1, h2[0])
                h2 = median_maintenance.heap_extract_min(h2)
            if len(h2) > len(h1):
                median = h2[0]
            else:
                median = h1[0]
            median_sum += median
            num_medians += 1
        return median_sum, num_medians

    # Helper method to insert for heap built for extracting maximumus
    def heap_insert_max(heap, value):
        heap.append(value)
        heap = median_maintenance.bubble_up_max(heap, len(heap)-1)
        return heap

    def bubble_up_max(heap, position):
        parent_position = (position-1) // 2
        if position != 0 and heap[parent_position] < heap[position]:
            heap[parent_position], heap[position] = heap[position], heap[parent_position]
            position = parent_position
            median_maintenance.bubble_up_max(heap, position)
        return heap

    # Helper method to insert for heap built for extracting minimums
    def heap_insert_min(heap, value):
        heap.append(value)
        heap = median_maintenance.bubble_up_min(heap, len(heap)-1)
        return heap

    def bubble_up_min(heap, position):
        parent_position = (position-1) // 2
        if position != 0 and heap[parent_position] > heap[position]:
            heap[parent_position], heap[position] = heap[position], heap[parent_position]
            position = parent_position
            median_maintenance.bubble_up_min(heap, position)
        return heap

    # Helper method for extracting max from heap
    def heap_extract_max(heap):
        heap[0] = heap.pop()
        heap = median_maintenance.bubble_down_max(heap, 0)
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
            median_maintenance.bubble_down_max(heap, position)
        elif left_child_position <= len(heap)-1 and heap[position] < heap[left_child_position]:
            heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
            position = left_child_position
            median_maintenance.bubble_down_max(heap, position)
        return heap

    # Helper method for extracting min from heap
    def heap_extract_min(heap):
        heap[0] = heap.pop()
        heap = median_maintenance.bubble_down_min(heap, 0)
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
            median_maintenance.bubble_down_min(heap, position)
        elif left_child_position <= len(heap)-1 and heap[position] > heap[left_child_position]:
            heap[position], heap[left_child_position] = heap[left_child_position], heap[position]
            position = left_child_position
            median_maintenance.bubble_down_min(heap, position)
        return heap


if __name__ == '__main__':
    started = datetime.datetime.now()
    object = median_maintenance('median_maintenance_with_heaps/median_maintenance.txt')
    print(object.median_sum)
    ended = datetime.datetime.now()
    runtime = ended - started
    print("Runtime: ", runtime)
