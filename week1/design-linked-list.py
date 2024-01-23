class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        curr = self.dummy.next
        count = 0 
        while curr:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        return -1


    def addAtHead(self, val: int) -> None:
        new_n = Node(val)
        new_n.next = self.dummy.next
        self.dummy.next = new_n


    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        new_n = Node(val)
        curr.next = new_n

        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        count = -1
        
        while curr:
            if count == index -1:
                new_n = Node(val)
                new_n.next = curr.next
                curr.next = new_n
                return 
            count += 1
            curr = curr.next
    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy
        count = 0
        while curr:
            if count == index and curr.next:
                curr.next = curr.next.next
            count += 1
            curr = curr.next

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)