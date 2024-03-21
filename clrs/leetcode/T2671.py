from collections import Counter


class FrequencyTracker:

    def __init__(self):
        self.mp = Counter()
        self.feq = Counter()

    def add(self, number: int) -> None:
        self.feq[self.mp[number]] -= 1
        self.mp[number] += 1
        self.feq[self.mp[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.mp[number] == 0:
            return
        self.feq[self.mp[number]] -= 1
        self.mp[number] -= 1
        self.feq[self.mp[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.feq[frequency] > 0
