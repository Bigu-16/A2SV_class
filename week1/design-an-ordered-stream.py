class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n+1)

        self.ptr = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        result = []

        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            result.append(self.stream[self.ptr])
            self.ptr += 1

        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

    # self.stream = [None] * (n + 1)
    #     # Pointer to the current position in the stream
    #     self.ptr = 1

    # def insert(self, idKey: int, value: str) -> List[str]:
    #     # Insert the pair into the stream
    #     self.stream[idKey] = value

    #     result = []

    #     # Check if the inserted pair completes a chunk
    #     while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
    #         # Append the value to the result and move the pointer
    #         result.append(self.stream[self.ptr])
    #         self.ptr += 1

    #     return result