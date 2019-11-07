
## HOMEWORK2      HEAP SORT 學習歷程＆流程圖
  
*  參考資料：https://www.geeksforgeeks.org/python-program-for-heap-sort/


```python
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
```


```python
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]) 
```

    Sorted array is
    5
    6
    7
    11
    12
    13


以上是我從網路上查詢到的程式碼，我自己想到的部分會跟這個程式碼所重疊，但後面想不到，所以決定了解網路上的程式碼後再重新自己打過一遍。


```python
def heapify(nums,n,i):
    max=i
    left=i*2+1
    right=i*2+2
    if nums[left]>nums[i]: 
        max=left
    if nums[right]>nums[i]:
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(0,n,1):
        heapify(nums,n,i)
    
    for i in range(n,-1,-1):
        nums[max],nums[i]=nums[i],nums[max]  
        heapify(nums, i, 0) 
```


```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-4-7c5b83f52dd3> in <module>
          1 nums = [ 12, 11, 13, 5, 6, 7]
    ----> 2 heapsort(nums)
    

    <ipython-input-3-60930776a243> in heapsort(nums)
         15     n=len(nums)
         16     for i in range(0,n,1):
    ---> 17         heapify(nums,n,i)
         18 
         19     for i in range(n,-1,-1):


    <ipython-input-3-60930776a243> in heapify(nums, n, i)
         10     if  max!=i:
         11         nums[i],nums[max]=nums[max],nums[i]
    ---> 12         heapify(nums, n, max)
         13 
         14 def heapsort(nums):


    <ipython-input-3-60930776a243> in heapify(nums, n, i)
          5     if nums[left]>nums[i]:
          6         max=left
    ----> 7     if nums[right]>nums[i]:
          8         max=right
          9 


    IndexError: list index out of range


這裡是我自己重新打過一次後的程式碼，發生了錯誤
而我便觀察nums[max],nums[i]=nums[i],nums[max]這行，我發現應該是跟 [o]換，因為這裡已經跑完了 heapify，所以最上面的值已經會是最大的值，在這個for迴圈裡面我沒有設變數叫Max，所以應該用 [o]


```python
def heapify(nums,n,i):
    max=i
    left=i*2+1
    right=i*2+2
    if nums[left]>nums[i]:
        max=left
    if nums[right]>nums[i]:
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(0,n,1):
        heapify(nums,n,i)
    
    for i in range(n,-1,-1):
        nums[0],nums[i]=nums[i],nums[0]   #max改成nums[0]
        heapify(nums, i, 0) 
```


```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-20-7c5b83f52dd3> in <module>
          1 nums = [ 12, 11, 13, 5, 6, 7]
    ----> 2 heapsort(nums)
    

    <ipython-input-19-6f174540b3a8> in heapsort(nums)
         15     n=len(nums)
         16     for i in range(0,n,1):
    ---> 17         heapify(nums,n,i)
         18 
         19     for i in range(n,-1,-1):


    <ipython-input-19-6f174540b3a8> in heapify(nums, n, i)
         10     if  max!=i:
         11         nums[i],nums[max]=nums[max],nums[i]
    ---> 12         heapify(nums, n, max)
         13 
         14 def heapsort(nums):


    <ipython-input-19-6f174540b3a8> in heapify(nums, n, i)
          5     if nums[left]>nums[i]:
          6         max=left
    ----> 7     if nums[right]>nums[i]:
          8         max=right
          9 


    IndexError: list index out of range


重新改過後發現還是錯的，看了他的錯誤訊息我覺得應該是range有問題，於是我重新看了一次range的定義，以for迴圈來講解的話，假如我打了：
for i in range(0, 4, 1) :
print(i)-->0,1,2,3
第一個位置的數"0"代表起始值，第二個位置的數"4"代表結束值，會停在指定數字的前一值，最後一個位置的數"1"代表每次增加或減少的值，所以如果是：
for i in range(4, 1, -1):
print(i)-->4,3,2
而這邊的概念是要把最後一個數值跟樹最上面的數值交換，因為數列的位置是第一個數值是0，第二個是1，以此類推，所以最後一個的數值的位置會是n-1，我在這裡把for i in range(n,-1,-1):改成for i in range(n-1,-1,-1):，應該要從最後一個數值的位置開始跑這個迴圈。


```python
def heapify(nums,n,i):
    max=i
    left=i*2+1
    right=i*2+2
    if nums[left]>nums[i]: 
        max=left
    if nums[right]>nums[i]:
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(0,n,1):
        heapify(nums,n,i)
    
    for i in range(n-1,-1,-1):   #range(n,-1,-1)改成range(n-1,-1,-1)
        nums[0],nums[i]=nums[i],nums[0]  
        heapify(nums, i, 0)  
```


```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-31-7c5b83f52dd3> in <module>
          1 nums = [ 12, 11, 13, 5, 6, 7]
    ----> 2 heapsort(nums)
    

    <ipython-input-30-e3bba593634c> in heapsort(nums)
         15     n=len(nums)
         16     for i in range(0,n,1):
    ---> 17         heapify(nums,n,i)
         18 
         19     for i in range(n-1,-1,-1):   #range(n,-1,-1)改成range(n-1,-1,-1)


    <ipython-input-30-e3bba593634c> in heapify(nums, n, i)
         10     if  max!=i:
         11         nums[i],nums[max]=nums[max],nums[i]
    ---> 12         heapify(nums, n, max)
         13 
         14 def heapsort(nums):


    <ipython-input-30-e3bba593634c> in heapify(nums, n, i)
          5     if nums[left]>nums[i]:
          6         max=left
    ----> 7     if nums[right]>nums[i]:
          8         max=right
          9 


    IndexError: list index out of range


這裡發現還是錯的，我決定從其他的問題解決，看heapify的這段，在這邊我卡了很久，我覺得好像有少了條件但一直想不到，後來上網重看了一次heapsort的定義以及樹的畫法，發現了假如個樹她下面的兩個孩子是不存在的，那就不能比，但我的程式碼沒有寫到此步驟，所以我便在if nums[left]>nums[i]: 
跟if nums[right]>nums[i]:多加上<n，改成if "left<n and "nums[left]>nums[i]: 跟 if "right<n and" nums[right]>nums[i]:，假如left小於n才能，因為要小於n才能等於是有東西在那個位置的，以此類推，right也要小於n才行。


```python
def heapify(nums,n,i):
    max=i
    left=i*2+1
    right=i*2+2
    if left<n and nums[left]>nums[i]: 
        max=left
    if right<n and nums[right]>nums[i]:
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(0,n,1):
        heapify(nums,n,i)
    
    for i in range(n-1,-1,-1):   
        nums[0],nums[i]=nums[i],nums[0]  
        heapify(nums, i, 0)  
```


```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
```


```python
nums
```




    [5, 11, 6, 7, 12, 13]



在這邊跑出答案時，我還以為成功了，但跑出的數列卻不是排序過後的，於是我又再檢查了一次我的程式碼，這邊大概卡了二三十分鐘，我終於發現  if right<n and nums[right]>nums[i]:這行好像有出錯，因為我認為概念跟上一行一樣所以沒有注意到，假如left比i大，那max就會變成left，這樣right就不該跟i來比較，因該是跟現在的max比較，所以改成了if right<n and nums[right]>nums[max]:


```python
def heapify(nums,n,i): 
    max=i
    left=i*2+1
    right=i*2+2
    if left<n and nums[left]>nums[i]: 
        max=left
    if right<n and nums[right]>nums[max]:  #nums[i]改成nums[max]
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(0,n,1):
        heapify(nums,n,i)
    
    for i in range(n-1,-1,-1):  
        nums[0],nums[i]=nums[i],nums[0]  
        heapify(nums, i, 0)  
```


```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
```


```python
nums
```




    [5, 6, 7, 11, 12, 13]



在這邊終於成功了，而我對照了一下最原始的程式碼，其實整體的邏輯概念幾乎是一樣的，除了變數以外，最大的差別是原始程式碼是for i in range(n, -1, -1): 
，而我在重新思考時的邏輯是for i in range(0,n,1):，原始程式碼是從最後面的位置往前看，設成i後一個一個代入，而我的想法是從樹的最上面往下看，而終點是n-1，也就是最後一個位置，所以中間的數設成n，這樣就會停在n-1。

但後來我發現用其他測值其實我這樣會是錯的


```python
nums = [3,7,9,11,3,7,-1,5] 
heapsort(nums) 
nums
```




    [-1, 3, 3, 5, 7, 7, 11, 9]




```python
def heapify(nums,n,i): 
    max=i
    left=i*2+1
    right=i*2+2
    if left<n and nums[left]>nums[i]: 
        max=left
    if right<n and nums[right]>nums[max]:  #nums[i]改成nums[max]
        max=right
   
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       
        heapify(nums, n, max) 
        
def heapsort(nums):
    n=len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums,n,i)
    
    for i in range(n-1,-1,-1):  
        nums[0],nums[i]=nums[i],nums[0]  
        heapify(nums, i, 0) 
```


```python
nums = [3,7,9,11,3,7,-1,5] 
heapsort(nums) 
nums
```




    [-1, 3, 3, 5, 7, 7, 11, 9]




```python
nums = [ 12, 11, 13, 5, 6, 7] 
heapsort(nums) 
nums
```




    [5, 6, 7, 11, 12, 13]



後來我發現，我原本的邏輯是錯的，因為如果從上往下看的話，有可能下面的值會比較大，所以會發生錯誤，而如果從最後面往前看，就不會出現這個錯誤。


```python
## 解釋整個程式碼：
##一開始跑的順序是  

def heapsort(nums):    # nums為隨便的數列
    n=len(nums)           # n=隨便的數列的長度
    for i in range(n-1, -1, -1):      # range在上面有提過，從樹的最下面往上跑，把i設為其中的數值，帶入heapify中
        heapify(nums,n,i)  #而他會放在這是因為他需要丟回heapify，而我們應該要先定義heapify才能夠丟進去，所以要放在定義 heapify後
   ##以上主要是為了建立樹 

##再來是:

def heapify(nums,n,i):     # 定義heapify
    max=i                      #先把最大值設為i，也就是樹的樹根
    left=i*2+1
    right=i*2+2             #為了比較左邊的孩子跟右邊的，所以設定這個方程式
    if left<n and nums[left]>nums[i]: 
        max=left            #這裡上面提過，主要是如果左邊的孩子是存在的且大於i的話就讓左邊的孩子變成max
    if right<n and nums[right]>nums[max]:  #nums[i]改成nums[max]
        max=right         #這裡上面也提過，如果右邊的孩子是存在的且大於現在的max的話就讓右邊的孩子變成max
    if  max!=i:
        nums[i],nums[max]=nums[max],nums[i]       # 假如max不等於i時，便把max的位置跟i的位置互換   
        heapify(nums, n, max) 
    ##這邊是讓我們跑出一個排列過的最大值樹，用第一步驟的for的迴圈代入來跑heapify    
          
##最後是：
    
    for i in range(n-1,-1,-1):   # 這邊上面提過了，應該要從最後一個數值的位置開始跑這個迴圈
        nums[0],nums[i]=nums[i],nums[0]     # heapsort的概念是排序過後要把最上面的值換成最後的值
        heapify(nums, i, 0)       #這邊我一開始理解花了很久的時間，不懂為什麼不用寫把最大值切除的程式碼，
                                         #後來了解到他是把heapify(nums, i, 0)有點像帶入 heapify(nums,n,i)的感覺
    ##這邊是讓最大值與最後的值交換，交換後整個數值需要重新排列，所以需要重新heapify，用for迴圈代入來跑heapify，最後可以求到排列過後的值    
```

## 改成助教的格式


```python
class Solution(object):
    def heapsort(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
                  
    def heapify(self, nums, n, i):
        max = i 
        left = i * 2 + 1
        right = i * 2 + 2
        if left < n and nums[left] > nums[i]:
            max = left
        if right < n and nums[right] > nums[max]:  
            max = right

        if max != i:
            nums[i], nums[max] = nums[max], nums[i]
            self.heapify(nums, n, max) 
```


```python
a=[8,3,5,1,0,-3,4]
Solution().heapsort(a)
print (a)
```

    [-3, 0, 1, 3, 4, 5, 8]



```python
 
```


# 流程圖
 ![](/image/heap%20sort流程圖.jpg)

