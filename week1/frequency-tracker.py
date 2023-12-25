class FrequencyTracker:

    def __init__(self):
        self.FrequencyTracker = []
        self.tracker = defaultdict(int)
        self.fTracker = defaultdict(int)

    def add(self, number: int) -> None:
        self.fTracker[self.tracker[number]] -= 1
        self.tracker[number] += 1
        self.fTracker[self.tracker[number]] += 1

        self.FrequencyTracker.append(number)

    def deleteOne(self, number: int) -> None:
        if number in self.FrequencyTracker:
            self.fTracker[self.tracker[number]] -= 1
            self.tracker[number] -= 1
            self.fTracker[self.tracker[number]] += 1

            self.FrequencyTracker.remove(number)

    def hasFrequency(self, frequency: int) -> bool:
        if self.fTracker[frequency] > 0:
            return True
        else:
            return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)