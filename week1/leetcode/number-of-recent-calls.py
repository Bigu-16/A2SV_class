class RecentCounter:

    def __init__(self):
        self.count = []

    def ping(self, t: int) -> int:
        if self.count:
            while self.count and self.count[0] < t - 3000:
                self.count = self.count[1:]
            self.count.append(t)
        else:
            self.count.append(t)

        return len(self.count)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)