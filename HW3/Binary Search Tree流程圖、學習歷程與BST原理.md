
## HW3 BST
## 參考資料: https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
# https://buptldy.github.io/2016/05/09/2016-05-09-Python%20BST/
# https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# https://github.com/jay940059/-/blob/master/HW3/binary_search_tree_06170221.py 的modify


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

以上是我之前打的linked-list，下面是先打insert


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        self.root = root
        # self.root.left = None
        # self.root.right = None
        if self.root is None:
            self.root = TreeNode(root)
        else:
            if val <= self.root.val:
                if self.root.left is None:
                    self.root.left = TreeNode(val)

                else:
                    return self.insert(root.left, val)

            elif val > self.root.val:
                if self.root.right is None:
                    self.root.right = TreeNode(val)

                else:
                    return self.insert(root.right, val)
```


```python
root1 = TreeNode(5)
Solution().insert(root1, 3)
Solution().insert(root1, 7)
print(Solution().insert(root1,4)==root1.left.right)
print(root1.left.right.val)
print(Solution().insert(root1, 4).val)
```

    False
    4



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-2-2d170ccb2fdb> in <module>
          4 print(Solution().insert(root1,4)==root1.left.right)
          5 print(root1.left.right.val)
    ----> 6 print(Solution().insert(root1, 4).val)
    

    AttributeError: 'NoneType' object has no attribute 'val'


問過後覺得應該不用多加self.root，因為上面的 __init__沒有root的值，這樣要比較複雜，所以我把self.root全部改掉


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
            self.left = None
            self.right = None
            if root is None:
                root = TreeNode(root)
            else:
                if val <= root.val:
                    if self.left is None:
                        self.left=TreeNode(val)
                    else:
                        self.insert(left,val)
                elif val > root.val:
                    if self.right is None:
                        self.right=TreeNode(val)
                    else:
                        self.insert(right,val)
```


```python
root1 = TreeNode(5)
Solution().insert(root1, 3)
Solution().insert(root1, 7)
print(Solution().insert(root1,4)==root1.left.right)
print(root1.left.right.val)
print(Solution().insert(root1, 4).val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-5-978a8b2ed0a0> in <module>
          2 Solution().insert(root1, 3)
          3 Solution().insert(root1, 7)
    ----> 4 print(Solution().insert(root1,4)==root1.left.right)
    

    AttributeError: 'NoneType' object has no attribute 'right'


我這邊發現不應該找self.left或self.right，可以直接說是root的左邊或是右邊，所以改成root.left，root.right


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insert(root.right, val)
        return TreeNode(val)
```


```python
root1 = TreeNode(5)
Solution().insert(root1, 3)
Solution().insert(root1, 7)
print(Solution().insert(root1,4)==root1.left.right)
print(root1.left.right.val)
print(Solution().insert(root1, 4).val)
```

    False
    4
    4


好這邊我卡了五個小時，為什麼兩個值是一樣但是是False，我想了很久想到了跟上次一樣的有可能是return的問題，return root、return root.left、return root.right


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    self.insert(root.right, val)
```


```python
root1 = TreeNode(5)
Solution().insert(root1, 3)
Solution().insert(root1, 7)
print(Solution().insert(root1,4)==root1.left.right)
print(root1.left.right.val)
print(Solution().insert(root1, 4).val)
```

    False
    4



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-10-2d170ccb2fdb> in <module>
          4 print(Solution().insert(root1,4)==root1.left.right)
          5 print(root1.left.right.val)
    ----> 6 print(Solution().insert(root1, 4).val)
    

    AttributeError: 'NoneType' object has no attribute 'val'


結果發現還是錯了，我隨便試試看加return，但這邊還不知道是為什麼，加上else: return self.insert(root.left, val) 跟 else: return self.insert(root.right, val)


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
```


```python
root1 = TreeNode(5)
Solution().insert(root1, 3)
Solution().insert(root1, 7)
print(Solution().insert(root1,4)==root1.left.right)
print(root1.left.right.val)
print(Solution().insert(root1, 4).val)
```

    True
    4
    4


對了！！！！！！好我insert用了一天半，目前來看看為什麼加上else: return self.insert(root.left, val) 跟 else: return self.insert(root.right, val)，在自己的函式中呼叫自己的函式，要加上return，原本沒加return的時候 最後一步insert完return新增的node位置 但遞迴還沒跑完所以他又回跑回去上一層的跑道的地方 但沒有return的時候接下來就沒東西了 ，所以她沒回傳任何東西 但加了一個return就是代表insert這個動作 但你做完了，所以他會return新增的node

再來打search，因為我覺得這個會比delete簡單


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
    def search(self, root, target):
        self.root=root
        # self.root.left = None
        # self.root.right = None
        if self.root is None:        
            return None
        else:
            if target < self.root.val:
                if self.root.left is None:
                    return None
                else:
                    self.search(root.left,target)
            elif target > self.root.val:
                if self.root.right is None:
                    return None
                else:
                    self.search(root.right,target)
            else:
                return self.root
```


```python
n=TreeNode(5)
n.left = TreeNode(3)
n.left.left=TreeNode(3)
n. left.left.left = TreeNode(-5)
n.right=TreeNode(8)
n.right.left=TreeNode(7)
n.right.left.left=TreeNode(6) 
n.right.right = TreeNode(10) 
print(Solution().search(n,-5)==n.left.left.left)
```

    False


因為我這邊跟insert其實是一起打的，所以我的想法是一樣錯的，一樣我把self.root全部改掉，也把self.left那些改掉，改成root.left，root.right


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
    def search(self, root, target):
            self.left = None
            self.right = None
            if root == None:        
                return 
            else:
                if target < root.val:
                    if self.left is None:
                        return None
                    else:
                        self.left.search(root,target)
                elif target > root.val:
                    if self.right is None:
                        return None
                    else:
                        self.right.search(root,target)
                else:
                    return root
```


```python
n=TreeNode(5)
n.left = TreeNode(3)
n.left.left=TreeNode(3)
n. left.left.left = TreeNode(-5)
n.right=TreeNode(8)
n.right.left=TreeNode(7)
n.right.left.left=TreeNode(6) 
n.right.right = TreeNode(10) 
print(Solution().search(n,-5)==n.left.left.left)
```

    False


然後一樣加上return


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
    def search(self, root, target):
        root.left=None
        root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    self.root.left.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    root.right.search(root.right,target)
            else:
                root
```


```python
n=TreeNode(5)
n.left = TreeNode(3)
n.left.left=TreeNode(3)
n. left.left.left = TreeNode(-5)
n.right=TreeNode(8)
n.right.left=TreeNode(7)
n.right.left.left=TreeNode(6) 
n.right.right = TreeNode(10) 
print(Solution().search(n,-5)==n.left.left.left)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-6149dca57c68> in <module>
          7 n.right.left.left=TreeNode(6)
          8 n.right.right = TreeNode(10)
    ----> 9 print(Solution().search(n,-5)==n.left.left.left)
    

    AttributeError: 'NoneType' object has no attribute 'left'


一樣在最後加上else: return root


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):     
        #root.left=None
        #root.right=None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
n=TreeNode(5)
n.left = TreeNode(3)
n.left.left=TreeNode(3)
n. left.left.left = TreeNode(-5)
n.right=TreeNode(8)
n.right.left=TreeNode(7)
n.right.left.left=TreeNode(6) 
n.right.right = TreeNode(10) 
print(Solution().search(n,-5)==n.left.left.left)
```

    True



```python
root1 = TreeNode(5)
node2 = Solution().insert(root1, 3)
node3 = Solution().insert(root1, 7)
print(Solution().search(root1,4)==root1.left.right)
```

    True


對了！！！！！！好我search用了快多了，最大的問題也在return

再來是delete


```python
def minValueNode( node): 
    current = node 
    while(current.left is not None): 
        current = current.left  
  
    return current  
def deleteNode(root, key): 
    if root is None: 
        return root  

    if key < root.key: 
        root.left = deleteNode(root.left, key) 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
    else: 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 
        root.key = temp.key 
        root.right = deleteNode(root.right , temp.key)   
    return root  
```

以上是網路上的範例，我理解過後用自己的方式打。


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):     
        #root.left=None
        #root.right=None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
                
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node 
    
    def delete(self, root, target):
        root = self.search(root,target)     
        if   root== None:
            return None
        if   root.val == target: 
            if   root.left is None and root.right is None:
                root = None
                return None
            elif root.left is not None and  root.right is None: 
                root=   root.left
                return root.left
            elif  root.left is None and  root.right is not None:  
                root =   root.right
                return root.right
            else: 
                a = self.maxValueNode(root.left)   
                root.val =a.val 
                root.left = self.delete(root.left,a.val)  
            return root  
        
    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print(Solution().insert(root1, 4) == root1.left.right)
# delete
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    True
    False



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-16445ca37699> in <module>
         24 root2 = Solution().delete(root2,3)
         25 print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
    ---> 26 print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
         27 print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
         28 print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)


    AttributeError: 'NoneType' object has no attribute 'right'


因為他說找不到right，我認為有可能是
*     elif root.left is not None and  root.right is None: 
                root=   root.left
                return root.left
              elif  root.left is None and  root.right is not None:  
                root =   root.right
                return root.right
                
 有問題，沒有讓他知道什麼是left什麼是right，而且root應該要變成none，所以改成  
 
 * elif  root.left is None and  root.right is not None:      
                a = root.right
                root = None
                return a
            else: 
                a = self.maxValueNode(root.left)   
                root.val =a.val 
                root.left = self.delete(root.left,a.val)  
            return root  


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):     
        #root.left=None
        #root.right=None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
                
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node 
    
    def delete(self, root, target):
        root = self.search(root,target)     
        if   root== None:
            return None
        if   root.val == target: 
            if   root.left is None and root.right is None:
                root = None
                return None
            elif root.left is not None and  root.right is None: 
                a = root.left
                root = None
                return a
            elif  root.left is None and  root.right is not None:      
                a = root.right
                root = None
                return a
            else: 
                a = self.maxValueNode(root.left)   
                root.val =a.val 
                root.left = self.delete(root.left,a.val)  
            return root  
        
    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print(Solution().insert(root1, 4) == root1.left.right)
# delete
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    True
    False



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-8-16445ca37699> in <module>
         24 root2 = Solution().delete(root2,3)
         25 print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
    ---> 26 print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
         27 print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
         28 print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)


    AttributeError: 'NoneType' object has no attribute 'right'



```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):     
        #root.left=None
        #root.right=None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
                
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node 
    
    def delete(self, root, target):
        if root is None: 
            return root  
        if target > root.val:
            root.right = self.delete(root.right, target)
        elif target < root.val:
            root.left = self.delete(root.left, target)
        elif  root.val == target:  
            if   root.left is None and root.right is None:
                root = None
                return None
            elif root.left is not None and  root.right is None: 
                a = root.left
                root = None
                return a
            elif  root.left is None and  root.right is not None:      
                a = root.right
                root = None
                return a
            else: 
                a = self.maxValueNode(root.left)   
                root.val =a.val 
                root.left = self.delete(root.left,a.val)  
            return root  
 
    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print(Solution().insert(root1, 4) == root1.left.right)
# delete
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    True



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-10-16445ca37699> in <module>
         23 # delete
         24 root2 = Solution().delete(root2,3)
    ---> 25 print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
         26 print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
         27 print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)


    AttributeError: 'NoneType' object has no attribute 'val'


這邊我想成不要用serch，改成用範例的方式從頭找起，所以改成
 * if root is None: 
            return root  
        if target > root.val:
            root.right = self.delete(root.right, target)
        elif target < root.val:
            root.left = self.delete(root.left, target)


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node
    def delete(self, root, target):
        if root is None:
            return root
        if target > root.val:
            root.right = self.delete(root.right, target)
        elif target < root.val:
            root.left = self.delete(root.left, target)
        elif  root.val == target:  
            if   root.left is None and root.right is None:
                root = None
                return None
            elif root.left is not None and  root.right is None: 
                a = root.left
                root = None
                return a
            elif  root.left is None and  root.right is not None:      
                a = root.right
                root = None
                return a
            elif root.left is not None and root.right is not None:
                a = self.maxRightNode(root.left)
                root.val = a.val
                root.left = self.delete(root.left, a.val)          
            return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print(Solution().insert(root1, 4) == root1.left.right)
# delete
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    True



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-16445ca37699> in <module>
         23 # delete
         24 root2 = Solution().delete(root2,3)
    ---> 25 print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
         26 print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
         27 print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)


    AttributeError: 'NoneType' object has no attribute 'val'


我想到把else寫得更清楚，於是改成         
*         elif root.left is not None and root.right is not None:
                a = self.maxRightNode(root.left)
                root.val = a.val
                root.left = self.delete(root.left, a.val)          
            return root
            


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node
    def delete(self, root, target):
        if root is None:
            return root
        if target > root.val:
            root.right = self.delete(root.right, target)
        elif target < root.val:
            root.left = self.delete(root.left, target)
        elif  root.val == target:  
            if   root.left is None and root.right is None:
                root = None
                return None
            elif root.left is not None and  root.right is None: 
                a = root.left
                root = None
                return a
            elif  root.left is None and  root.right is not None:      
                a = root.right
                root = None
                return a
            elif root.left is not None and root.right is not None:
                a = self.maxRightNode(root.left)
                root.val = a.val
                root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print(Solution().insert(root1, 4) == root1.left.right)
# delete
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    True
    False
    True
    True
    True


然後我想到了我最後的return縮排的位置不太對，我想要的應該是在elif  root.val == target:最後return，所以我改了縮排，然後發現一些是true了，而false我看了一兩天才發現是因為我這樣不能刪掉重複的值


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
```


```python
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print("insert")
print(Solution().insert(root1, 4) == root1.left.right)
print("------------------------------------------")
# delete
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
print("------------------------------------------")
# search
print("search")
print(Solution().search(root2, 10) == root2.right.right)
print("------------------------------------------")
```

    insert
    True
    ------------------------------------------
    delete
    True
    True
    True
    True
    ------------------------------------------
    search
    True
    ------------------------------------------


對啦！！！！我這邊把       
* if root is None:
            return root
            
改回我原本想用search的方式，因為我想到的方式是要用while迴圈，所以要用search，改成
 *       while self.search(root,target) != None:

再來用modify


```python
    def modify(self, root, target, new_val):
        count = 0 #假設一個變數為 0
        temp = Solution().search(root,target) 
        while temp is not None and temp.val == target:
            count += 1
            temp = temp.left           
        Solution().delete(root,target)
        
        for i in range(count):
            Solution().insert(root,new_val)
        return root
```

以上是參考同學的modify的程式碼


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else: 
            self.delete(root,target)
            k=0                                          
            a=self.search(root,target)
            if a==None:
                return root   
                while a != None and a.val == target:
                    k=k+1
                    a=a.left          
                while k>0:
                    self.insert(root,new_val)
                return root            
```


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
root = Solution().modify(root,7,4)
print(root.right.left.val)
print(root.left.right.val)
```

    6



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-6-55c1a0fe23c0> in <module>
          9 root = Solution().modify(root,7,4)
         10 print(root.right.left.val)
    ---> 11 print(root.left.right.val)
    

    AttributeError: 'NoneType' object has no attribute 'val'


好，這邊是錯的，我想了一段時間後想到，假如我在一開始就把要刪掉的值都刪掉了，那我後來當然會search不到，所以我把delete移到後面


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else: 
            k=0                                          
            a=self.search(root,target)
            if a==None:
                return root    
            else:
                while a != None and a.val == target:
                    k=k+1
                    a=a.left  
                self.delete(root,target)
                while k>0:
                    self.insert(root,new_val)
                return root          
```


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
root = Solution().modify(root,7,4)
print(root.right.left.val)
print(root.left.right.val)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-8-55c1a0fe23c0> in <module>
          7 root.right.left.left = TreeNode(6)
          8 root.right.right = TreeNode(10)
    ----> 9 root = Solution().modify(root,7,4)
         10 print(root.right.left.val)
         11 print(root.left.right.val)


    <ipython-input-7-1a378f1c6ed4> in modify(self, root, target, new_val)
         85             self.delete(root,target)
         86             while k>0:
    ---> 87                 self.insert(root,new_val)
         88             return root


    <ipython-input-7-1a378f1c6ed4> in insert(self, root, val)
         18                     return root.left
         19                 else:
    ---> 20                     return self.insert(root.left, val)
         21             elif val > root.val:
         22                 if root.right is None:


    <ipython-input-7-1a378f1c6ed4> in insert(self, root, val)
         24                     return root.right
         25                 else:
    ---> 26                     return self.insert(root.right, val)
         27         return TreeNode(val)
         28 


    <ipython-input-7-1a378f1c6ed4> in insert(self, root, val)
         18                     return root.left
         19                 else:
    ---> 20                     return self.insert(root.left, val)
         21             elif val > root.val:
         22                 if root.right is None:


    ... last 1 frames repeated, from the frame below ...


    <ipython-input-7-1a378f1c6ed4> in insert(self, root, val)
         18                     return root.left
         19                 else:
    ---> 20                     return self.insert(root.left, val)
         21             elif val > root.val:
         22                 if root.right is None:


    RecursionError: maximum recursion depth exceeded


這邊我發現了應該是k出了問題
*          while k>0:
                self.insert(root,new_val)
              
我在這邊沒有多寫東西的話，k永遠會是>0的，所以我加了
*          while k>0:
                self.insert(root,new_val)
                k=k-1


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        # root.left = None
        # root.right = None
        if root is None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right, val)
        return TreeNode(val)
    
    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        while self.search(root,target) != None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)          
        return root

    def search(self, root, target):
        #root.left=None
        #root.right=None
        if root == None:        
            return 
        else:
            if target < root.val:
                if root.left is None:
                    return None
                else:
                    return self.search(root.left,target)
            elif target > root.val:
                if root.right is None:
                    return None
                else:
                    return self.search(root.right,target)
            else:
                return root
    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else: 
            k=0                                          
            a=self.search(root,target)
            if a==None:
                return root    
            else:
                while a != None and a.val == target:
                    k=k+1
                    a=a.left  
                self.delete(root,target)
                while k>0:
                    self.insert(root,new_val)
                    k=k-1
                return root 
```


```python
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
root = Solution().modify(root,7,4)
print(root.right.left.val)
print(root.left.right.val)
```

    6
    4


對了！！！！在這邊終於打完全部，還好改成禮拜五晚上交，不然不可能打得出來，連續熬夜好多天終於對了，但是不知道有沒有bug拉....


```python

```
# 流程圖
 ![](.jpg)
# 流程圖
 ![](.jpg)
# 流程圖
 ![](.jpg)
# 流程圖
 ![](.jpg)
