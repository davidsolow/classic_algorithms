class median_maintenance(object):
    """
    Maintains the median in a set of values as additional values are added.

    Args:
        values_file = a list of integers
    """

    def __init__(self, values_file):
        self.values = []
        with open(values_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.values.append(line)
