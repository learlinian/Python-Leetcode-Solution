from bisect import bisect


class HitCounter(object):

    def __init__(self):
        self.dp = []
        self.timestamp = []

    def hit(self, timestamp):
        if len(self.dp) == 0:
            self.dp.append(1)
            self.timestamp.append(timestamp)
        elif timestamp == self.timestamp[-1]:
            self.dp[-1] += 1
        else:
            self.dp.append(self.dp[-1] + 1)
            self.timestamp.append(timestamp)

    def getHits(self, timestamp):
        if len(self.timestamp) == 0 or timestamp - self.timestamp[-1] >= 300:
            return 0
        expiry_index = bisect(self.timestamp, timestamp-300)
        return self.dp[-1] - self.dp[expiry_index - 1] if expiry_index >= 1 else self.dp[-1]
