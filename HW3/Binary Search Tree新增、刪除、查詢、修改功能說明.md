
## Binary Search Tree新增、刪除、查詢、修改功能說明
## 參考資料: https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
# https://buptldy.github.io/2016/05/09/2016-05-09-Python%20BST/
# https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# https://github.com/jay940059/-/blob/master/HW3/binary_search_tree_06170221.py 的modify

## 新增功能說明

* insert(新增資料)：要在BST中新增node(新增資料)

而我這邊的想法是，我一開始先看樹根有沒有東西，如果沒有的話那插入的這個值就會是樹根，所以我寫了    
*  def insert(self, root, val):        
        if root is None:
            root = TreeNode(val)
            return root
            
再來就是要看其餘的，也就是樹根有值的時候，如果我要丟入的值會小於或等於樹根時，然後樹根的左邊的值又沒有值時，丟入的值就會是樹根左邊的值
*          else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left
                    
一樣在樹根有值的時候，如果我要丟入的值會小於或等於樹根時，但樹根的左邊的值有值時，就要把樹根的左邊重新丟到這個def，把樹根的左邊當成新的樹根
 *                else:
                    return self.insert(root.left, val)
                    
樹根有值的時候，如果我要丟入的值會大於樹根時，然後樹根的右邊的值又沒有值時，丟入的值就會是樹根右邊的值 
*             elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right
      
一樣在樹根有值的時候，如果我要丟入的值會大於樹根時，但樹根的右邊的值有值時，就要把樹根的右邊重新丟到這個def，把樹根的右邊當成新的樹根 
*                 else:
                    return self.insert(root.right, val)
                    
這樣就可以把我要丟入的值放到正確的位置上


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object): 
    def insert(self, root, val):              #定義insert這個函數 
        if root is None:                       
            root = TreeNode(val)
            return root                       #如果root是沒有值的val就是root的值
        else:
            if val <= root.val:          
                if root.left is None:
                    root.left = TreeNode(val)
                    return root.left          #如果root有值且val小於等於root的值，然後root的左邊沒值，那val就是root.left的值
                else:
                    return self.insert(root.left, val)   #如果root有值且val小於等於root的值，但root的左邊有值，那就把root.left當成root丟回insert這個函數
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return root.right       #如果root有值且val大於root的值，然後root的右邊沒值，那val就是root.right的值
                else:
                    return self.insert(root.right, val)    #如果root有值且val大於root的值，但root的右邊有值，那就把root.right當成root丟回insert這個函數
```

## 刪除功能說明

* delete(刪除資料):刪除不能直接把節點與其子點全部移除，要讓樹保持二元搜索樹的定義，有三種情況要考慮：

   1.沒有子節點時，可以直接移除 
   
   2.有一個子節點時，將子節點取代被移除的節點的位置
   
   3.有兩個子節點，可以從左子樹找到最大值或右子樹找到最小值的節點，來取代被移除的節點位置
   
我這邊的想法是一開始去找我要刪的值在哪裡，是不是存在的，所以跑我設定的serch函數，用while是因為如果有重複值那就可以一次刪掉
*         while self.search(root,target) != None:

而如果要刪的值大於樹根的值，那就讓樹的右邊當成樹根再去跑一次這個def，而如果要刪的值小於樹根的值，那就讓樹的左邊當成樹根再去跑一次這個def
*           if target > root.val:
                root.right = self.delete(root.right, target)
              elif target < root.val:
                root.left = self.delete(root.left, target)   
                
而如果要刪的值等於樹根的值，樹的左右都沒有值，所以直接刪掉，是上面的1.狀況，如果樹的左右其中一個有值，就取代被移除的節點，是上面的2.狀況
*              if   root.left is None and root.right is None:
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
                    
如果要刪的值等於樹根的值，樹的左右都有值，是上面的3.狀況，要找左邊最大的值或是右邊最小的值來取代，所以我設定了一個max函數，可以找到最右邊的位置也就是最大的值
*    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node
  
然後運用函數找到左邊最大的值去取代現在要刪掉的位置，再把移上去的值的原本位置刪掉
*             elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val
                    root.left = self.delete(root.left, a.val)   
                
這樣就可以把要刪掉的值刪掉，且保持原本樹的規格


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def maxValueNode(self, node):          #定義maxValueNode的函數
        while node.right is not None:
            node = node.right
        return node                #如果node.right沒東西，那就把node當成node.right，一直跑while迴圈，跑到最後右邊沒有東西時，回傳最下面那個值
 
    def delete(self, root, target):            #定義delete的函數
        while self.search(root,target) != None:    #跑search函數看我要刪的值有沒有存在如果還存在就會一直跑這個函式
            if target > root.val:
                root.right = self.delete(root.right, target)    #要刪的值大於樹根的值，那就讓root.right當成root再去跑一次這個def
            elif target < root.val:
                root.left = self.delete(root.left, target)      #要刪的值小於樹根的值，那就讓root.left當成root再去跑一次這個def
            elif  root.val == target:  
                if   root.left is None and root.right is None:
                    root = None
                    return None                    #要刪的值等於樹根的值，root.left跟right都沒有值，直接刪掉
                elif root.left is not None and  root.right is None: 
                    a = root.left
                    root = None
                    return a
                elif  root.left is None and  root.right is not None:      
                    a = root.right
                    root = None
                    return a                       # 要刪的值等於樹根的值，root.left或right其中一個有值，root.left或right就取代被移除的節點
                elif root.left is not None and root.right is not None:
                    a = self.maxRightNode(root.left)
                    root.val = a.val              #要刪的值等於樹根的值，root.left跟right都有值，找root.left最大的值，跑maxValueNode函數可找出，被移除的節點
                    root.left = self.delete(root.left, a.val)  # 再把移上去的值的原本位置刪掉，讓root.left當成root再去跑一次這個def
        return root
```

## 查詢功能說明

* search(搜尋資料)：在處理資料時，需要尋找某特定資料是否存在資料結構中。

而我這邊的想法是，我一開始先看樹根有沒有東西，如果沒有的話那就會不可能找到東西，這個樹會不存在，所以我寫了      
* class Solution(object):
     def search(self, root, target):
        if root == None:        
            return 
            
再來就是要看樹根有值的時候，如果我要找的值會小於樹根的值，然後樹根的左邊的值又沒有值時，就會不可能找到東西
*        else:
            if target < root.val:
                if root.left is None:
                    return None
                    
一樣在樹根有值的時候，如果我要找的值會小於樹根的值，但樹根的左邊的值存在時，就要把樹根的左邊重新丟到這個def，把樹根的左邊當成新的樹根
 *                else:
                    return self.search(root.left,target)
                    
樹根有值的時候，如果我要找的值會大於樹根的值，然後樹根的右邊的值又沒有值時，就會不可能找到東西
*             elif target > root.val:
                if root.right is None:
                    return None
      
一樣在樹根有值的時候，如果我要找的值會大於樹根的值，但樹根的右邊的值存在時，就要把樹根的右邊重新丟到這個def，把樹根的右邊當成新的樹根 
*                 else:
                    return self.search(root.right,target)
                    
如果樹根有值的時候，且我要找的值等於樹根的值，那就知道樹根的數值就是我要找的值的位置
*           else:
                return root
                
這樣就可以找到我想找到的值


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def search(self, root, target):                #定義search這個函數 
        #root.left=None
        #root.right=None
        if root == None:        
            return                                      #如果root是沒有值的，那val不可能被找到，因為樹是空的
        else:
            if target < root.val:
                if root.left is None:
                    return None                  #如果root有值且target小於root的值，然後root的左邊沒值，那也是找不到           
                else:
                    return self.search(root.left,target) #如果root有值且target小於root的值，然後root的左邊有值，那就把root.left當成root丟回search這個函數    
            elif target > root.val:
                if root.right is None:
                    return None                 #如果root有值且target大於root的值，然後root的右邊沒值，那也是找不到
                else:
                    return self.search(root.right,target)#如果root有值且target大於root的值，然後root的右邊有值，那就把root.right當成root丟回search這個函數    
            else:
                return root    #如果root有值且target等於root的值，那就找到了target的位置   
```

## 修改功能說明

* modify(修改資料)：刪掉指定的資料並改成要插入的值，並讓樹還是保持二元搜索樹的定義

因為我想不到最好的方式，所以我目前的想法是先看我要刪掉的值跟後來修改的值一不一樣，一樣的話就不用改變
*      if target == new_val:
            return root
            
不一樣的話就先設定一個變數，且去跑search函式，讓我知道有幾個數值要修改
*       else: 
            k=0                                          
            a=self.search(root,target)
            while a != None and a.val == target:
                k=k+1
                a=a.left  

假如根本沒有這個數值可以刪除，就不用改變
*          if a==None:
                return root  

把要刪掉的值丟進delete中全部刪掉
*   self.delete(root,target)

用insert把我要改成的值插入
*      while k>0:
                self.insert(root,new_val)
                k=k-1
             return root  


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def modify(self, root, target, new_val):  #定義modify的函數
        if target == new_val:     
            return root                  #我要刪掉的值target跟new_val一樣不用改變
        else: 
            k=0                                          
            a=self.search(root,target)    #target跟new_val不一樣，先設定k=0 ，丟去跑search函數找，a設為此
            if a==None:                     
                return root                  #假如a不存在，就不用改變      
            else:                       
                while a != None and a.val == target:
                    k=k+1
                    a=a.left   #假如a存在，跑while迴圈，若a存在且a的值等於target，k就加上1，然後把a.left當成a，繼續跑迴圈，這樣就可以知道有幾個要刪的值
                self.delete(root,target)   #丟到delete函式，刪除我們要刪掉的值
                while k>0:
                    self.insert(root,new_val)   #跑while迴圈，假如k>0，就丟入insert，插入我們要加的值
                    k=k-1                #每加入一個值，k就-1，一直去跑while
                return root            #如果k等於或小於0就停止
```


```python

```
