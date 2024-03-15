class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * (k)
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        
        if not self.isFull():
            self.rear += 1
            self.rear = self.rear % len(self.queue)
            self.queue[self.rear] = value
            if self.isEmpty():
                self.front += 1
            return True
        
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
                self.front = self.front % len(self.queue) 
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        # print(self.rear)
        if self.queue and self.rear != -1:
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return True if self.front == -1 else False

    def isFull(self) -> bool:
        # print(self.front,self.rear, len(self.queue))

        if (self.front == 0 and self.rear == len(self.queue)-1) or self.front - self.rear == 1:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()