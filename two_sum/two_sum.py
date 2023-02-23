class two_sum:
    def __init__(self, data):
        self.values = {}
        with open(data,m 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.values[int(line)] = 0
        self.number_of_two_sums = two_sum.solve(self.values)

    def solve(values):
        for t, i in range(-10000, 10001), values.values:
            y = t - i
