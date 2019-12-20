
# HW5 BFS與DFS
## 參考資料：
#### https://www.itread01.com/content/1542363063.html
#### https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
#### https://alanwalker.me/2019/04/06/Python实现BFS-DFS/
#### https://codereview.stackexchange.com/questions/192147/depth-first-search-of-graph-in-python

 ----------------------------------------
##   BFS與DFS原理與比較 
### 原理
####  BFS
定義

以某一節點為出發點，先拜訪所有相鄰的節點。再拜訪與剛才被拜訪過的節點相鄰但未曾被拜訪過的節點，直到所有相鄰的節點都已被拜訪過。 
需要使用 queue ，以便記錄拜訪的順序。以樹來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。

概念

 * 首先將起點放入queue中。

 * 從queue中取出第一個節點，並檢驗它是否為目標。

    *  如果找到目標，則結束搜尋並回傳結果。
   
    *  找出跟此點相鄰的點，且尚未拜訪的點，依照編號順序放入queue
   
 * 重複上面步驟直到queue為空，表示整張圖都檢查過了


####  DFS
定義

「先遇到的點就先探索」，以某一節點為出發點，不斷前進拜訪未曾被拜訪過的節點， 直到無路可走或是所有相鄰的節點都已經拜訪過為止，然後再退回前一個節點，尋找沒有拜訪過的節點，直到所有相鄰的節點都已被拜訪過。

概念

* 將起始頂點 v 放入stack 中

* 從 stack 取出一點 w 

  * 若w未走訪過，走訪w否則跳回上面步驟
  
  * 將與 w 相鄰且尚未拜訪過的所有頂點依序放入 stack 中 
  
* 重複上面步驟直到stack 為空，表示整張圖都檢查過了

 ----------------------------------------
### 比較
####  BFS

利用queue

Queue：排隊，不能插隊。一次只能執行一個需求，需要用 Queue來安排執行順序。（影印機印紙一次印一張）

* Pop：把front最前面所指向的資料從Queue中移除

####  DFS

DFS

利用stack

Stack：「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」

* Pop：把「最晚進入Stack」的資料移除。

 ----------------------------------------

## 學習歷程


```python
# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```

以上是助教給的格式，先從BFS開始想


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s): 
        queue = []
        explored = []
        queue.append(s) 
        
        while len(queue) > 0:
            v = queue.pop(0)
            if v not in explored:
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
        return explored
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(2) 
```




    [0, 3]



好這邊是錯的，開始找問題點，首先我第一個想到的是應該要多加上 explored.append(v)  
*           if v not in explored:

改成
*           if v not in explored:
                explored.append(v)  


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s): 
        queue = []
        explored = []
        queue.append(s) 
        
        while len(queue) > 0:
            v = queue.pop(0)
            if v not in explored:
                explored.append(v)  
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
        return explored
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(2) 
```




    [2, 0, 3]



這邊會缺少最後一個值，但頭的值已經有跑出來了，所以我決定多設一個集合，更清楚表達我所想的，所以我多設了visited，讓我整個流程更清楚，
*         while len(queue) > 0:
            v = queue.pop(0)
            if v not in explored:
                explored.append(v)  
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
                        
改成
*       visited = []
        
          while len(queue) > 0:
            v = queue.pop(0)
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s): 
        queue = []
        explored = []
        queue.append(s) 
        visited = []
        
        while len(queue) > 0:
            v = queue.pop(0)
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
        return explored
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(2) 
```




    [2,
     0,
     3,
     2,
     0,
     1,
     2,
     2,
     0,
     3,
     3,
     2,
     0,
     3,
     2,
     0,
     1,
     2,
     2,
     0,
     3,
     2,
     0,
     1,
     2,
     2,
     0,
     3,
     2,
     0,
     1,
     2,
     2,
     0,
     3,
     3,
     2,
     0,
     3,
     2,
     0,
     1,
     2,
     2,
     0,
     3,
     3,
     2,
     0,
     3,
     2,
     0,
     1,
     2]



這邊跑出一大串，重新看過後我發現我要看得並不是explored，應該是visited
*         return explored

改成
*         return visited


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s): 
        queue = []
        explored = []
        queue.append(s) 
        visited = []
        
        while len(queue) > 0:
            v = queue.pop(0)
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        queue.append(j)
        return visited
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2) )
```

    [2, 0, 3, 1]


對了！又試試我其他的測值


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 0) 
g.addEdge(1, 2)
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(4, 3) 
g.addEdge(5, 3) 
g.BFS(4)
```




    [4, 2, 3, 0, 1, 5]




```python
g = Graph() 
g.addEdge(1, 2)
g.addEdge(1, 4) 
g.addEdge(2, 3) 
g.addEdge(2, 5) 
g.addEdge(3, 1) 
g.addEdge(3, 5) 
g.addEdge(3, 6) 
g.addEdge(4, 7) 
g.addEdge(5, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(6, 8)
g.addEdge(7, 8)
g.BFS(1)
```




    [1, 2, 4, 3, 5, 7, 6, 8]



都是對的，接下來看看
### DFS


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def DFS(self, s): 
        stack = []
        explored = []
        stack.append(s) 
        visited = []
        
        while len(stack) > 0:
            v = stack.pop(0)
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        stack.append(j)
        return visited
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.DFS(2) )
```

    [2, 0, 3, 1]


我先改成stack，然後這邊都還是一樣的結果，stack跟 queue的差別在於pop的位置，一個是最後面丟的值，一個是第一個值，所以把
*         while len(stack) > 0:
               v = stack.pop(0)
            
改成
*         while len(stack) > 0:
                v = stack.pop()


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def DFS(self, s): 
        stack = []
        explored = []
        stack.append(s) 
        visited = []
        
        while len(stack) > 0:
            v = stack.pop()
            explored.append(v)  
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    explored.append(i)
                    for j in explored:
                        stack.append(j)
        return visited
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.DFS(2) )
```

    [2, 3, 0, 1]


這邊對了，然後再試試其他測值


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 0) 
g.addEdge(1, 2)
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(4, 3) 
g.addEdge(5, 3) 
g.DFS(4)
```




    [4, 3, 5, 2, 0, 1]



這邊看似對了但其實正確答案應該會是，435102，所以我繼續找錯誤，而這邊是我整趟作業卡最久的地方，我試著加上網路上的方式，
*        while len(stack) > 0:
              v = stack.pop()
              explored.append(v)  
              if v not in visited:
                  visited.append(v)
                  for i in self.graph[v]:
                      explored.append(i)
                      for j in explored:
                          stack.append(j)
           return visited
           
改成
*     while(len(stack) > 0):
            vertex = stack.pop()
            explored.append(vertex)
            visited.append(vertex)
            for i in self.graph[vertex]:
                if i not in explored:
                    stack.append(i)
                    explored.append(i)
          return visited    


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def DFS(self, s): 
        stack = []
        explored = []
        stack.append(s) 
        visited = []
        
        while(len(stack) > 0):
            vertex = stack.pop()
            explored.append(vertex)
            visited.append(vertex)
            for i in self.graph[vertex]:
                if i not in explored:
                    stack.append(i)
                    explored.append(i)
        return visited    
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.DFS(2) )
```

    [2, 3, 0, 1]



```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 0) 
g.addEdge(1, 2)
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(4, 3) 
g.addEdge(5, 3) 
g.DFS(4)
```




    [4, 3, 5, 1, 0, 2]



這邊是對的，於是我開始找兩個程式碼的差別，後來我用紙畫出整個流程，發現假如我沒有在最後面判斷       if i not in explored:這行的話，會出現一些錯誤的排序，因為stack的pop是看最後進來的值，所以會有差，於是我把
*        while len(stack) > 0:
              v = stack.pop()
              explored.append(v)  
              if v not in visited:
                  visited.append(v)
                  for i in self.graph[v]:
                      explored.append(i)
                      for j in explored:
                          stack.append(j)
           return visited
           
改成
*      while len(stack) > 0:
            v = stack.pop()
            explored.append(v)
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    if i not in explored:
                        explored.append(i)
                        for j in explored:
                            stack.append(j)
         return visited


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v)  
        
    def DFS(self, s):
        stack = []
        explored = []
        stack.append(s) 
        visited = []
        
        while len(stack) > 0:
            v = stack.pop()
            explored.append(v)
            if v not in visited:
                visited.append(v)
                for i in self.graph[v]:
                    if i not in explored:
                        explored.append(i)
                        for j in explored:
                            stack.append(j)
        return visited
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.DFS(2) )
```

    [2, 3, 0, 1]


是對的，繼續看其他值


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 0) 
g.addEdge(1, 2)
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(4, 3) 
g.addEdge(5, 3) 
g.DFS(4)
```




    [4, 3, 5, 1, 0, 2]




```python
g = Graph() 
g.addEdge(1, 2)
g.addEdge(1, 4) 
g.addEdge(2, 3) 
g.addEdge(2, 5) 
g.addEdge(3, 1) 
g.addEdge(3, 5) 
g.addEdge(3, 6) 
g.addEdge(4, 7) 
g.addEdge(5, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(6, 8)
g.addEdge(7, 8)
g.DFS(1)
```




    [1, 4, 7, 8, 2, 5, 6, 3]



成功了！！其實在這邊我發現，有可能是作業難度比較簡單許多（BST真的超難......），所以整體速度都提升很多，而且比較容易找到問題點，也比較能自己想出改進的地方，以前錯誤的時候要問同學才能找出癥結點，現在可以自己一人用出一份作業真的差很多，雖然沒有網路上最初的架構我還是無法打出作業，但我覺得已經比一開始進步很多了，一開始真的是弄得非常崩潰.....，希望之後可以試著自己打出架構！！！

### 正確版


```python
from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def BFS(self, s):     #定義BFS
        queue = []
        explored = []
        queue.append(s) 
        visited = []          #設定queue,explored,explored空集合，且把要加入的頂點丟入queue
        
        while len(queue) > 0:  #跑while迴圈，如果queue集合的長度大於0的話跑while
            v = queue.pop(0)    #v設定為queue集合第一個數
            explored.append(v) #把v丟入explored
            if v not in visited:    
                visited.append(v)   #如果v不在visited中，把v丟入visited
                for i in self.graph[v]:  #跑for迴圈，i為v指向的點
                    explored.append(i)  #把i丟入explored
                    for j in explored:  #跑for迴圈，j為explored中的點
                        queue.append(j) #把j丟入queue
        return visited  #回傳visited

    def DFS(self, s):     #定義DFS
        stack = []
        explored = []
        stack.append(s) 
        visited = []         #設定stack,explored,explored空集合，且把要加入的頂點丟入stack
        
        while len(stack) > 0:  #跑while迴圈，如果stack集合的長度大於0的話跑while
            v = stack.pop()     #v設定為stack集合加入的最後一個數
            explored.append(v) #把v丟入explored
            if v not in visited:
                visited.append(v)  #如果v不在visited中，把v丟入visited
                for i in self.graph[v]:   #跑for迴圈，i為v指向的點
                    if i not in explored:  
                        explored.append(i) #如果i不在explored裡，把i丟入explored
                        for j in explored: #跑for迴圈，j為explored中的點
                            stack.append(j) #把j丟入stack
        return visited  #回傳visited
```


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2) )
print(g.DFS(2) )
```

    [2, 0, 3, 1]
    [2, 3, 0, 1]



```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 0) 
g.addEdge(1, 2)
g.addEdge(1, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 2) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(4, 3) 
g.addEdge(5, 3) 
print(g.BFS(4) )
print(g.DFS(4) )
```

    [4, 2, 3, 0, 1, 5]
    [4, 3, 5, 1, 0, 2]



```python
g = Graph() 
g.addEdge(1, 2)
g.addEdge(1, 4) 
g.addEdge(2, 3) 
g.addEdge(2, 5) 
g.addEdge(3, 1) 
g.addEdge(3, 5) 
g.addEdge(3, 6) 
g.addEdge(4, 7) 
g.addEdge(5, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(6, 8)
g.addEdge(7, 8)
print(g.BFS(1) )
print(g.DFS(1) )
```

    [1, 2, 4, 3, 5, 7, 6, 8]
    [1, 4, 7, 8, 2, 5, 6, 3]



```python

```
