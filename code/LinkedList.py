class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0:
            return -1
        if index > self.size - 1: 
            return -1
        l = self.head  
        for i in range(index): 
            l = l.next  
        return l.data  

    def addAtHead(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size = self.size + 1
        else:
            newHead = Node(data)
            newHead.next = self.head
            self.head = newHead
            self.size = self.size + 1

    def addAtTail(self, data):
        l = self.head
        if self.head is None:
            self.head = Node(data)
            self.size = self.size + 1
        else:
            while l.next is not None:
                l = l.next
            l.next = Node(data)  
            self.size = self.size + 1

    def addAtIndex(self, index: int, data: int):
        if index == 0:
            self.addAtHead(data)
        elif index == self.size:
            self.addAtTail(data)
        elif index < self.size and index > 0:
            l = self.head
            for i in range(index - 1):  
                l = l.next 
            node = Node(data)  
            node.next = l.next  
            l.next = node  
            self.size += 1

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return
        l = self.head
        if index == 0:
            if l == None:
                return
            self.head = l.next
            self.size -= 1
        else:
            for i in range(index - 1):  
                l = l.next  
            l.next = l.next.next  
            self.size -= 1
