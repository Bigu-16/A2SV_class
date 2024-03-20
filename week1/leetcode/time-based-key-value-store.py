class TimeMap:

    def __init__(self):
        self.map_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map_dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ''
        values = self.map_dict.get(key,[])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)