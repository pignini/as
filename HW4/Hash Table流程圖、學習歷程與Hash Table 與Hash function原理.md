
# HW4 hash table
#  參考資料:
http://linebylinecode.com/2017/11/24/how-to-implement-a-hash-table-in-python

https://codereview.stackexchange.com/questions/118110/python-hash-table-implementation

https://www.youtube.com/watch?v=zHi5v78W1f0&t=298s

 ----------------------------------------
  
### Hash Function

是一種輸入字串，然後輸出數字的函數。也就是「將字串對應至數字」。

密碼學的觀點：資料進行編碼，以求隱蔽，保護資料。

例： “Apple” → Hash Function → 3

這次是使用MD5來加密。

 ----------------------------------------
### Hash Table

使用Hash Function，將丟入的值對應到符合Table大小中，Table的意思像是在array裡創很多條的linked list，找到對應的值丟進去。

 ----------------------------------------
### 兩者的作用原理：
 * 將一個特定的名稱對應於相同的數字，每次輸入Apple，都會得到相同的數字(例如 3)。
 * 將不同的字串對應至不同的值，有一點小小的變化值都會差很多。例： Apple 對應至3，Milk 對應至 4
 * 雜湊函數知道陣列的大小，而且只傳回有效的索引值。
透過雜湊函數與陣列的結合，可得到一個Hash Table資料結構。
 ----------------------------------------

```python
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
```

以上是我之前打的linked-list


```python
from Crypto.Hash import MD5
```


```python
h = MD5.new()
h.update("GOT7".encode("utf-8"))
print (h.hexdigest())
x=h.hexdigest()
x=int(h.hexdigest(),16)
print(x)
```

    12476f6314f51e9b46e2bb449f936cde
    24297016198624584279060826097601178846


上面是我先試試看著個功能，照著老師上課的程式碼打的


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
```

以上是助教給的格式，再來我先試著把MD5用成一個def，這樣就可以不用重複呼叫


```python
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
        h.update("key".encode("utf-8"))
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
```


```python
hashSet=MyHashSet()
hashSet.hash_function("dog")
hashSet.hash_function("pig")
```

    3c6e0b8a9c15224a8228b9a98ca1531d
    80325066489831061459460196859901989661
    3c6e0b8a9c15224a8228b9a98ca1531d
    80325066489831061459460196859901989661





    1



在這邊我試著帶入兩得不同的值，但發現出來的編碼是一樣的，所以我猜測可能是
* "key"不應該有""，所以我刪去了""


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
```


```python
hashSet=MyHashSet()
hashSet.hash_function("dog")
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845





    0




```python
hashSet.hash_function("pig")
```

    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312





    2



這邊兩個出來的答案就不一樣了，所以確定是對的，接下來我先用add


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            while node.head.next is not None:
                node.head = node.head.next  
            node.head.next = ListNode(key) 
```

這邊我用到了一些自己打linked-list的觀念，還有上次BST的部分，這邊因為還沒有contains所以我不能使用助教的測值測試，但我自己在想後面的時候想到了一個問題，我沒有講head的部分所以我覺得不要多打head比較好，而且其實意思是差不多一樣的所以我把
*            node.head = node.head.next  
             node.head.next = ListNode(key) 
             
改成
*            node = node.next  
             node.next = ListNode(key) 


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            while node.next is not None:
                node = node.next  
            node.next = ListNode(key) 
```

再來是先打contains來確定我上面的是對的


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            while node.next is not None:
                node = node.next  
            node.next = ListNode(key) 

    def contains(self, key):
        index = self.hash_function(key)
        node = self.data[index]  
        if node == None:
            return False
        else:
            while node is not None:
                node = node.next
                return True
            else: 
                return False
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    True
    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    True
    d077f244def8a70e5ea758bd8352fcd8
    277102220249073555409885156483852860632
    True


好這邊cat不應該是True但卻出現了，所以開始找錯誤，其實我算蠻快就看到了，因為我自己想的邏輯是這樣但打出來卻沒有對上，
*            while node is not None:
                     node = node.next
                      return True 
        
這邊我的想法是如果遇到那個編碼得值便停下且回傳True，但這樣打並不會呈現我的想法，所以我改成

*            while node is not None and node.val != key:
                     node = node.next
                      return True


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            while node.next is not None:
                node = node.next  
            node.next = ListNode(key) 

    def contains(self, key):
        index = self.hash_function(key)
        node = self.data[index]  
        if node == None:
            return False
        else:
            while node is not None and node.val != key:
                node = node.next
                return True
            else: 
                return False
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    False
    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    False
    d077f244def8a70e5ea758bd8352fcd8
    277102220249073555409885156483852860632
    True


答案變成完全錯誤，但其實這邊我也有預想到會是錯的，因為暫時想不出解決方法，所以我先打出來試試，而在這邊我想了一下到底要怎麼呈現自己的邏輯，於是我改成
*     def contains(self, key):
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
                
多加了if node is not None:，才會是找到我要找得值的意思


```python
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
        print (h.hexdigest())
        x=int(h.hexdigest(),16)
        print(x)
        y = x % self.capacity
        return y
        
    def add(self, key):
        index = self.hash_function(key)
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(key)
            return
        else:
            while node.next is not None:
                node = node.next  
            node.next = ListNode(key) 

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
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    f74c6af46a78becb2f1bd3f95bbd5858
    328716098820163891201703637637140404312
    True
    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    True
    d077f244def8a70e5ea758bd8352fcd8
    277102220249073555409885156483852860632
    False


正確的了！！！然後在這之前我是為了要確認每個值得編碼是否不同，所以都print出來，現在不用了所以我把print刪掉
*    def hash_function(self, key):
          h = MD5.new()
           h.update(key.encode("utf-8"))
           print (h.hexdigest())
            x=int(h.hexdigest(),16)
            print(x)
            y = x % self.capacity
            return y
        
 改成
 
*    def hash_function(self, key):
            h = MD5.new()
            h.update(key.encode("utf-8"))
           h.hexdigest()
             x=int(h.hexdigest(),16)
            y = x % self.capacity
             return y


```python
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
            while node.next is not None:
                node = node.next  
            node.next = ListNode(key) 

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
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
```

    True
    True
    False


好目前add跟contains都算正確了，接下來試試看remove


```python
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
                node = None
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
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    True


我認為這邊應該是跟contains很像，也是要找出在哪裡然後取代掉他，所以我便試著用contains的程式碼去改變，而這邊是錯的，所以我多家上一些想法，
*         if node is not None:
                node = None
                return 
                
改成
*          if node is not None:
                node= None
                node = node.next
                return 
                
這邊的想法是要把要刪掉的值刪去且把後面的值拉來這個位置


```python
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
                node= None
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
            
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-10-ac3983d73be9> in <module>
         11 rel=hashSet.contains("bird")
         12 print(rel)
    ---> 13 hashSet.remove("pig")
         14 rel=hashSet.contains("pig")
         15 print(rel)


    <ipython-input-9-daec7eb43fe5> in remove(self, key)
         40             if node is not None:
         41                 node= None
    ---> 42                 node = node.next
         43                 return
         44             else:


    AttributeError: 'NoneType' object has no attribute 'next'


這邊又出現了問題，而我認為應該會是一樣的地方出錯，所以又改了一次，這次試試看加上.val
*          if node is not None:
                node= None
                node = node.next
                return 
            
改成
*        if node is not None:
                node.val = None
                node.val = node.val.next
                return 


```python
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
                node.val = node.val.next
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
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-27-ac3983d73be9> in <module>
         11 rel=hashSet.contains("bird")
         12 print(rel)
    ---> 13 hashSet.remove("pig")
         14 rel=hashSet.contains("pig")
         15 print(rel)


    <ipython-input-26-cbbb6a0796c3> in remove(self, key)
         51             if node is not None:
         52                 node.val = None
    ---> 53                 node.val = node.val.next
         54                 return
         55             else:


    AttributeError: 'NoneType' object has no attribute 'next'


好這邊還是錯的，所以我換了一個想法，假如我是刪掉要刪掉的直裡的數，然後把後面的整個node壓上來試試看
*           if node is not None:
                node.val = None
                node.val = node.val.next
                return 
                
改成
*          if node is not None:
                node.val = None
                node = node.next
                return 


```python
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
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    False


這邊成功了，但我發現假如插入重複的值，不能重複刪掉


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.add("pig")
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    True


在想要怎麼重複刪掉的時候我決定讓值不能重複加入，這樣就可以免除重複刪掉的問題，所以要從add中來改


```python
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
            
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    False



```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.add("pig")
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    False


原本以為成功了，後來發現我丟 ListNode(key)這樣不對，應該丟十進位後的，所以我改了hash_function的return，還有後面def裡的ListNode還有node.val不等於的對象


```python
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
        return x
        
    def add(self, key):
        index = self.hash_function(key) % self.capacity
        node = self.data[index]
        if node == None:
            self.data[index] = ListNode(self.hash_function(key))
            return
        else:
            if self.contains(key) is True:
                return
            else:
                while node.next is not None:
                    node = node.next  
                node.next = ListNode(self.hash_function(key)) 
           
    def remove(self, key):  
        index = self.hash_function(key) % self.capacity
        node = self.data[index]  
        if node == None:
            return
        else:
            while node is not None and node.val != self.hash_function(key):
                node = node.next
            if node is not None:
                node.val = None
                node = node.next
                return 
            else: 
                return   
        
    def contains(self, key):
        index = self.hash_function(key) % self.capacity
        node = self.data[index]  
        if node == None:
            return False
        else:
            while node is not None and node.val != self.hash_function(key) :
                node = node.next
            if node is not None:
                return True
            else: 
                return False
```


```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    False



```python
hashSet=MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel=hashSet.contains("bird")
print(rel)
hashSet.add("pig")
hashSet.remove("pig")
rel=hashSet.contains("pig")
print(rel)
```

    True
    True
    False
    True
    False


### 成功了！！！
我覺得這次功課我花的時間明顯比之前少上許多，可能是因為上次的作業以及寫過linked-list的觀念所以導致很快就可以想到問題在哪，雖然我還是沒辦法沒有參考資料和基本的大架構就寫出來整個程式碼，但至少已經可以比一開始好上許多，現在可以不問同學就自己寫出一份了，希望之後有辦法自己想出一個大架構，因為如果還是照著看參考資料的話永遠還是都會跟參考資料有很大的相似，可能還不能一次進步到自己想要的樣子，但至少已經比開學時的自己進步了許多！

程式碼說明


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def hash_function(self, key):       #定義hash_function
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()
        x=int(h.hexdigest(),16)           #設定MD5         
        return x                      
        
    def add(self, key):           #定義add
        index = self.hash_function(key) % self.capacity   #index是hash_function的結果，找出餘數找到對應的位置
        node = self.data[index]       #設定node為index的那條
        if node == None:
            self.data[index] = ListNode(self.hash_function(key))
            return           #如果node沒東西，那就把加入的key設為ListNode加進去
        else:
            if self.contains(key) is True:
                return          #丟進contains的def裡，如果是True，就return
            else:
                while node.next is not None:     #丟進contains的def裡，如果不是True，就跑while迴圈
                    node = node.next           #while迴圈，如果node下一個存在就一直跑，node會等於node的下一個
                node.next = ListNode(self.hash_function(key))  #node的下一個位置就把加入的key設為ListNode加進去
                
    def remove(self, key):           #定義remove
        index = self.hash_function(key) % self.capacity   #index是hash_function的結果，找出餘數找到對應的位置
        node = self.data[index]        #設定node為index的那條
        if node == None:
            return                  #假如node是None就return
        else:              #如果node不是None
            while node is not None and node.val != self.hash_function(key): 
                node = node.next      #跑while迴圈，node存在且node的值不是x時就一直跑，node會等於node的下一個                        
            if node is not None:      #跑到node的值是x時停下，假如此時node存在
                node.val = None
                node = node.next
                return                     #node的值就刪掉，node就會是node的下一個 ，return
            else:        
                return                      #跑到node的值是x時停下，假如此時node不存在就return
            
    def contains(self, key):         #定義contains
        index = self.hash_function(key) % self.capacity   #index是hash_function的結果，找出餘數找到對應的位置
        node = self.data[index]          #設定node為index的那條
        if node == None:
            return False                #假如node是None就return False
        else:            #如果node不是None
            while node is not None and node.val != self.hash_function(key):
                node = node.next      #跑while迴圈，node存在且node的值不是x時就一直跑，node會等於node的下一個  
            if node is not None:      #跑到node的值是x時停下，假如此時node存在就return True
                return True   
            else:                         #跑到node的值是x時停下，假如此時node不存在就return False              
                return False  
```


# 流程圖
 ![](/image/hash%20table.jpg)
