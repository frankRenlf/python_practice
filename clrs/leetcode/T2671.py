class FrequencyTracker:

    def __init__(self):
        self.mp = {}
        self.feq = {}

    def add(self, number: int) -> None:
        self.mp[number] = self.mp.get(number, 0) + 1

    def deleteOne(self, number: int) -> None:
        self.mp[number] = (
            self.mp.get(number, 0) - 1 if self.mp.get(number, 0) > 0 else 0
        )

    def hasFrequency(self, frequency: int) -> bool:
        for k, v in self.mp.items():
            if v == frequency:
                return True
        return False
