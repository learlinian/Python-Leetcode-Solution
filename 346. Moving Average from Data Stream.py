# runtime: 58%; memory: 28%

class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.values = []
        self.count = 0
        self.sum = 0

    def next(self, val):
        self.values.append(val)
        if self.count < self.size:
            self.sum += val
            self.count += 1
            return float(self.sum) / self.count
        else:
            self.sum = self.sum + val - self.values[0]
            del self.values[0]
            return float(self.sum) / self.size
