
# HW6     Dijkstra與Kruskal

## 參考資料：
## https://blog.csdn.net/u010558281/article/details/53905807
## https://www.jb51.net/article/149022.htm
## http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html


## https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
## https://gist.github.com/hayderimran7/09960ca438a65a9bd10d0254b792f48f
## https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
## https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
## https://github.com/wellslu/DSA/blob/master/week8/Dijkstra%26Kruskal.ipynb

 ----------------------------------------
##   Dijkstra與Kruskal原理 
####  Dijkstra  Shortest Path(最短路徑問題)

定義

以某一節點當作出發點，在與其相連且尚未被選取的節點裡，選擇加入離出發點距離最短的節點，並且透過新增的節點更新到達其他節點的距離。 如此重覆加入新節點，直到所有的節點都被加入為止。
「最短路徑」是由起點到終點、權重最小的路徑，可能有許多條，也可能不存在。起點到終點不通、不存在路徑的時候，就沒有最短路徑。
 * 性質：每一條最短路徑，都是由其它的最短路徑延展而得。一條最短路徑，截去末端之後，還是最短路徑。

概念

 *  至起始點找尋尚未拜訪的相鄰結點
 *  更新最短路徑表
 *  找尋目前未拜訪的最短路徑結點，將此結點設為起始點，並設為已拜訪
 *  重複第一步，直到所有結點皆為已拜訪
 
 ----------------------------------------

####  Kruskal  Minimum Spanning Tree(MST，最小生成樹)

定義

圖中具有weight（權重），不同的Spanning Tree有不同的weight總和，其中具有最小weight總和（權重總和最小）的樹，稱為最小生成樹

概念

* 連結圖中所有的點的樹
* 是樹，所以沒有cycle
* 是樹，若圖有V個點，就只有V−1條邊，E = V−1

 ----------------------------------------

## 學習歷程：


### 助教格式


```python
from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
```

首先來用 Dijkstra



```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    while nodes:  
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if new_distance < distance[d]:
                    distance[d]=new_distance
                visited.append(d) 
                nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-6-06d503e51c39> in <module>
          9           [0,0,2,0,0,0,6,7,0]
         10           ]
    ---> 11 Dijkstra(graph, 0)
    

    <ipython-input-5-10b7d7ff57af> in Dijkstra(graph, s)
          8 
          9     while nodes:
    ---> 10         for v in visited:
         11             for d in nodes:
         12                 new_distance = graph[s][v]+graph[v][d]


    KeyboardInterrupt: 


很棒一開始就直接來個無限迴圈，這邊我先加上
*      visited.append(s)
            nodes.remove(s)


```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    while nodes:
        visited.append(s)
        nodes.remove(s)
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if new_distance < distance[d]:
                    distance[d]=new_distance
                visited.append(d) 
                nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 8, 8: 0}



跑出東西了，但只有一些跑出來，我想可能是因為有0所以他會一直認為0最小，於是我多了一句 if  new_distance is not 0:，把
*        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if new_distance < distance[d]:
                    distance[d]=new_distance
                visited.append(d) 
                nodes.remove(d) 
                
改成
*         for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 


```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    while nodes:
        visited.append(s)
        nodes.remove(s)
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 8, 8: 0}



好一樣，再來看看distance[d]也有等於0的問題，所以把
*        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
                    
改成
*        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 


```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    while nodes:
        visited.append(s)
        nodes.remove(s)
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 12, 3: 8, 4: 4, 5: 4, 6: 4, 7: 8, 8: 15}



好暫時安慰自己有東西跑出來，因為打到這邊我已經快心態炸裂，現在來重新看一遍我的程式碼，我想了很久才發現因為助教給的測值沒有連接的話會是0，但我沒有判斷所以他會一直覺得有0這個距離，所以我加上了一些東西
*      new_distance = graph[s][v]+graph[v][d]
                if  new_distance is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
                    
改成
*       new_distance = graph[s][v]+graph[v][d]
                if  graph[s][v] is not 0 and graph[v][d] is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        graph[s][d]=new_distance
                        distance[d]=new_distance
                        visited.append(d) 
                        nodes.remove(d) 


```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    while nodes:
        visited.append(s)
        nodes.remove(s)
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  graph[s][v] is not 0 and graph[v][d] is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        graph[s][d]=new_distance
                        distance[d]=new_distance
                        visited.append(d) 
                        nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-28-06d503e51c39> in <module>
          9           [0,0,2,0,0,0,6,7,0]
         10           ]
    ---> 11 Dijkstra(graph, 0)
    

    <ipython-input-27-bc42c4b56358> in Dijkstra(graph, s)
          9     while nodes:
         10         visited.append(s)
    ---> 11         nodes.remove(s)
         12         for v in visited:
         13             for d in nodes:


    ValueError: list.remove(x): x not in list


好沒事一切都會好的：），我想到應該還是0判斷的部分跟while式還有問題
*  while nodes:
        visited.append(s)
        nodes.remove(s)
        for v in visited:
            for d in nodes:
                new_distance = graph[s][v]+graph[v][d]
                if  graph[s][v] is not 0 and graph[v][d] is not 0:
                    if distance[d]==0 or new_distance < distance[d]:
                        graph[s][d]=new_distance
                        distance[d]=new_distance
                        visited.append(d) 
                        nodes.remove(d) 
                        
改成
*   for i in distance:
        if distance[i]>0:
            nodes.remove(i)
        for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d)


```python
def Dijkstra(graph,s):
    nodes = [i for i in range(len(graph))]  
    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]  
    
    for i in distance:
        if distance[i]>0:
            nodes.remove(i)
    for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 8, 8: 0}



這邊我發現我把nodes全部都刪掉了，所以都會是0，因為根本看不到後面
*    for i in distance:
        if distance[i]>0:
            nodes.remove(i)
            
改成
*   for i in distance:
        if distance[i]>0:
            visited.append(i)
       nodes.remove(s)


```python
def Dijkstra(graph,s):
    nodes=[]
    for i in range(len(graph)):
        nodes.append(i)

    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]
    
    for i in distance:
        if distance[i]>0:
            visited.append(i)
    nodes.remove(s)
    for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 

    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 12, 3: 19, 4: 28, 5: 16, 6: 9, 7: 8, 8: 15}



有一些對了，而且也都沒有0，看了很久我發現是nodes的問題，我應該要每次都要跟前面的比較，不是看過就刪掉，所以
*   for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d) 
                    nodes.remove(d) 
                    
改成
*   for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d) 


```python
def Dijkstra(graph,s):
    nodes=[]
    for i in range(len(graph)):
        nodes.append(i)

    visited=[] 
    distance={s:0}  
    
    for i in nodes:
        distance[i]=graph[s][i]
    
    for i in distance:
        if distance[i]>0:
            visited.append(i)
    nodes.remove(s)
    for v in visited:
        for d in nodes:
            new_distance = graph[s][v]+graph[v][d]
            if  graph[s][v] is not 0 and graph[v][d] is not 0:
                if distance[d]==0 or new_distance < distance[d]:
                    graph[s][d]=new_distance
                    distance[d]=new_distance
                    visited.append(d) 

    return distance
```


```python
graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],    
          [0,0,2,0,0,0,6,7,0]
          ]
Dijkstra(graph, 0) 
```




    {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}



對了！我改成助教的格式


```python
from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def Dijkstra(self,s):
        nodes=[]
        for i in range(self.V):
            nodes.append(i)
            
        seen=[] 
        distance={s:0}  
    
        for i in nodes:
            distance[i]=self.graph[s][i]
    
        for i in distance:
            if distance[i]>0:
                seen.append(i)
        nodes.remove(s)
        for v in seen:
            for d in nodes:
                new = self.graph[s][v]+self.graph[v][d]
                if  self.graph[s][v] is not 0 and self.graph[v][d] is not 0:
                    if distance[d]==0 or new < distance[d]:
                        self.graph[s][d]=new
                        distance[d]=new
                        seen.append(d)
        return distance
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]

print('Dijkstra',g.Dijkstra(0))
```

    Dijkstra {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}



```python
from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 

    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    
    def Kruskal(self):
        seen=[]
        for i in range(self.V):
            seen.append(i)
            
        result={}
        for i in sorted(self.dict):
            for j,k in self.dict[i]:
                if seen[j] == seen[k]:
                    pass
                else:
                    seen = [seen[j] if x==seen[k] else x for x in seen]
                    result[str(j)+'-'+str(k)] = i
        return result
```


```python
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
print('Kruskal',g.Kruskal())
```

    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}



```python
from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def Dijkstra(self,s):
        nodes=[]
        for i in range(self.V):
            nodes.append(i)   #nodes設為全部的點
            
        seen=[] 
        distance={s:0}  #距離定出來
    
        for i in nodes:
            distance[i]=self.graph[s][i]   #初始化所有的距離
    
        for i in distance:
            if distance[i]>0:
                seen.append(i)        #把有位置的，且已知位置加seen，從seen去往下找
        nodes.remove(s)   #把s從nodes中去除，變成[1,2,3,4,5,6,7,8]
        for v in seen:       #v = 已有距離的點位
            for d in nodes:        #d = 1,2,3,4,5,6,7,8
                new = self.graph[s][v]+self.graph[v][d]      #new設為0到d的距離
                if  self.graph[s][v] is not 0 and self.graph[v][d] is not 0: #新距離兩者不等於0
                    if distance[d]==0 or new < distance[d]:        #如果距離d為0或者是new小於距離d
                        self.graph[s][d]=new
                        distance[d]=new                 #距離d跟self.graph[s][d]都改為new
                        seen.append(d)     #把d加入已有距離的點位
        return distance
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]

print('Dijkstra',g.Dijkstra(0))
```

    Dijkstra {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}


## 最終版本


```python
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
        
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
        
    def Dijkstra(self, s): 
        nodes=[]
        for i in range(self.V):
            nodes.append(i)
            
        seen=[] 
        distance={s:0}  
    
        for i in nodes:
            distance[i]=self.graph[s][i]
    
        for i in distance:
            if distance[i]>0:
                seen.append(i)
        nodes.remove(s)
        for v in seen:
            for d in nodes:
                new = self.graph[s][v]+self.graph[v][d]
                if  self.graph[s][v] is not 0 and self.graph[v][d] is not 0:
                    if distance[d]==0 or new < distance[d]:
                        self.graph[s][d]=new
                        distance[d]=new
                        seen.append(d)
        return distance
    
    def Kruskal(self):
        seen=[]
        for i in range(self.V):
            seen.append(i)
            
        result={}
        for i in sorted(self.dict):
            for j,k in self.dict[i]:
                if seen[j] == seen[k]:
                    pass
                else:
                    seen = [seen[j] if x==seen[k] else x for x in seen]
                    result[str(j)+'-'+str(k)] = i
        return result
```


```python
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]

print('Dijkstra',g.Dijkstra(0))

g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
print('Kruskal',g.Kruskal())
```

    Dijkstra {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}



```python

```


## Dijkstra與Kruskal流程圖
 ![](/image/Dijkstra.jpg)
