class RandomizedSet:

    def __init__(self):
        self.element = []
        self.element_dict = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.element_dict:
            self.element.append(val)
            self.element_dict[val] = len(self.element) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.element_dict:

            last_element, idx = self.element[-1], self.element_dict[val]
            self.element[idx], self.element[-1] = self.element[-1], self.element[idx]
            self.element_dict[last_element] = idx

            self.element.pop()
            del self.element_dict[val]
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.element)
