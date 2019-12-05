class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        index = key % self.capacity
        node = self.data[index]
        if self.contains(key) is True:
            return
        if self.contains(key) is  False:
            if node == None:
                self.data[index] = ListNode(key)
                return
            else:
                while node.next is not None:
                    node = node.next  
                node.next = ListNode(key) 

    def contains(self, key):
        index = key % self.capacity
        node = self.data[index]  
        if node == None:
            return False
        else:
            while node is not None and node.val != key:
                node = node.next
            if node is not None:
                return True
            else: 
                return False
            
    def remove(self, key):  
        index = key % self.capacity
        node = self.data[index]  
        if node == None:
            return
        else:
            while node is not None and node.val != key:
                node = node.next
            if node is not None:
                node.val = None
                node = node.next
                return 
            else: 
                return 
