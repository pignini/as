from Crypto.Hash import MD5
        
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def hash_function(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()
        x=int(h.hexdigest(),16)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            if self.contains(key) is True:
                return
            else:
                while node.next is not None:
                    node = node.next  
                node.next = ListNode(key) 
           
    def remove(self, key):  
        index = self.hash_function(key)
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
        
    def contains(self, key):
        index = self.hash_function(key)
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
            
#參考資料:
#http://linebylinecode.com/2017/11/24/how-to-implement-a-hash-table-in-python
#https://codereview.stackexchange.com/questions/118110/python-hash-table-implementation
#https://www.youtube.com/watch?v=zHi5v78W1f0&t=298s
