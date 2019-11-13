
## HOMEWORK2     Quick Sort 學習歷程＆流程圖

參考資料：https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239
           
參考資料： https://stackoverflow.com/questions/18262306/quicksort-with-python?fbclid=IwAR0dgPZVC-eDgIvKw2tXN_JcoNQNeZSzWHkvPHqWefqT9pIdqh-AV-w-NW4


```python
def quicksort(x):
      if len(x) < 2:      #如果數列中的數字長度不到兩個就不用跑下面的程式碼
          return x
      else:
          pivot = x[0]   #把數列的第一個數作為pivot
          less = [i for i in x[1:] if i < pivot] 
                             #比pivot小的放less數列裡， x[1:] 是把x從1(第二個位置的數)開始往後找，因為0是pivot
          more = [i for i in x[1:] if i >= pivot]     #大於等於的放more數列裡
          return quicksort(less) + [pivot] + quicksort(more) 
                            #把新的數列重整，把quicksort(less) 和quicksort(more)丟回if len(x) < 2:，若有兩個以上的數字，再重複上述步驟(選pivot、調整數列)
                           #直到所有list中都只剩下一個數，分不出「新的數列」為止，就會停止分類
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```




    [0, 1, 3, 4, 6, 8, 8, 9, 11, 16]



上面是我第一次的程式碼，再來我重打了一次，看了heap跟merge的程式碼後來改這個的程式碼


```python
def quicksort(nums):
    r=0
    l=0
    n=len(nums) 
    if n >= 2:  
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less[l]=nums[i]
                l=l+1
            else:
                more[r]=nums[i]
                r=r+1
        return quicksort(less) + [pivot] + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-e7179fcb494e> in <module>
          1 list=[4,8,3,0,11,8,16,1,6,9]
    ----> 2 quicksort(list)
    

    <ipython-input-1-aa3d330f4020> in quicksort(nums)
          7         for i in nums:
          8             if i<pivot:
    ----> 9                 less[l]=nums[i]
         10                 l=l+1
         11             else:


    NameError: name 'less' is not defined


好開始找錯誤，這邊我認為是因為我沒有設定less跟more的集合，所以他不知道要丟進哪裡所以我多設了    less=[]  more=[]


```python
def quicksort(nums):
    r=0
    l=0
    n=len(nums) 
    if n >= 2:  
        less=[]
        more=[]
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less[l]= nums[i]
                l=l+1
            else:
                more[r]= nums[i]
                r=r+1
        return quicksort(less) + [pivot] + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-4-e7179fcb494e> in <module>
          1 list=[4,8,3,0,11,8,16,1,6,9]
    ----> 2 quicksort(list)
    

    <ipython-input-3-e1d07b6f1a35> in quicksort(nums)
          9         for i in nums:
         10             if i<pivot:
    ---> 11                 less[l]= nums[i]
         12                 l=l+1
         13             else:


    IndexError: list assignment index out of range


這邊我改進了less跟more的問題了，但我發現不應該是less[l]= nums[i]和more[r]= nums[i]，我原本以為是不應該有nums，所以我改成 less[l]= i跟more[r]=i


```python
def quicksort(nums):
    r=0
    l=0
    n=len(nums) 
    if n >= 2:  
        less=[]
        more=[]
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less[l]= i
                l=l+1
            else:
                more[r]=i
                r=r+1
        return quicksort(less) + [pivot] + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-6-e7179fcb494e> in <module>
          1 list=[4,8,3,0,11,8,16,1,6,9]
    ----> 2 quicksort(list)
    

    <ipython-input-5-a34f8d55adb3> in quicksort(nums)
          9         for i in nums:
         10             if i<pivot:
    ---> 11                 less[l]= i
         12                 l=l+1
         13             else:


    IndexError: list assignment index out of range


後來我上網查發現，不能用a[0] = i，你只能用append，對python來說此時 a 的第0個位置是不存在的，因為他的長度是 0，所以我只能你只能 a.append(2)，所以我改成less.append(i)跟more.append(i)


```python
def quicksort(nums):
    n=len(nums) 
    if n >= 2:  
        less=[]
        more=[]
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less.append(i)
            else:   
                more.append(i)
        return quicksort(less) + [pivot] + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-e7179fcb494e> in <module>
          1 list=[4,8,3,0,11,8,16,1,6,9]
    ----> 2 quicksort(list)
    

    <ipython-input-7-3de3a8bd0916> in quicksort(nums)
         10             else:
         11                 more.append(i)
    ---> 12         return quicksort(less) + [pivot] + quicksort(more)
    

    <ipython-input-7-3de3a8bd0916> in quicksort(nums)
         10             else:
         11                 more.append(i)
    ---> 12         return quicksort(less) + [pivot] + quicksort(more)
    

    TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'


好，卡住了......，我覺得應該要加上else，不然長度小於2就沒辦法丟回去，所以長度小於2的回傳倒nums，所以加了    if n < 2: return nums else:


```python
def quicksort(nums):
    n=len(nums) 
    if n < 2:
        return nums
    else:  
        less=[]
        more=[]
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less.append(i)
            else:   
                more.append(i)
        return quicksort(less) + [pivot] + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-10-e7179fcb494e> in <module>
          1 list=[4,8,3,0,11,8,16,1,6,9]
    ----> 2 quicksort(list)
    

    <ipython-input-9-f76831a742cb> in quicksort(nums)
         12             else:
         13                 more.append(i)
    ---> 14         return quicksort(less) + [pivot] + quicksort(more)
    

    ... last 1 frames repeated, from the frame below ...


    <ipython-input-9-f76831a742cb> in quicksort(nums)
         12             else:
         13                 more.append(i)
    ---> 14         return quicksort(less) + [pivot] + quicksort(more)
    

    RecursionError: maximum recursion depth exceeded while calling a Python object


在這邊卡住了，上網查後發現了有一個方法跟我現在的程式碼很像，而他跟我的差別在他多設定了一個[]，後來發現，假如我沒有多設定那個[]，那跟pivot一樣的會一直丟回去，應該丟到一個其他的[]才能跑，於是多加了mid=[]，和elif i == pivot:   mid.append(i) ，而現在假如i等於pivot時丟進mid，所以return quicksort(less) + [pivot] + quicksort(more)改成return quicksort(less) + mid + quicksort(more)
* ==是等于，比较对象是否相等    一模一樣的、相等的，但本質上這是兩個不同的對象
* =簡單的運算符號


```python
def quicksort(nums):
    n=len(nums) 
    if n < 2:
        return nums
    else:  
        mid=[]
        less=[]
        more=[]
        pivot=nums[n//2] 
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i == pivot:
                mid.append(i)
            else:   
                more.append(i)
        return quicksort(less) + mid + quicksort(more)
```


```python
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
```




    [0, 1, 3, 4, 6, 8, 8, 9, 11, 16]



# 解釋整個程式碼：


```python
def quicksort(nums):   
    n=len(nums)         #把nums的變數長度設為n
    if n < 2:
        return nums   #如果數列中的數字長度不到兩個就不用跑下面的程式碼
    else:  
        mid=[]
        less=[]
        more=[]        #mid,less,more設空集合
        pivot=nums[n//2]    #把數列的中間數作為pivot，//是除後取整數的意思
        for i in nums:         #把i帶入nums的數
            if i<pivot:         
                less.append(i)   #如果i小於pivot，就把i丟進less
            elif i == pivot:
                mid.append(i)    #如果i等於pivot，就把i丟進mid
            else:   
                more.append(i)  #如果i大於pivot，就把i丟進more
        return quicksort(less) + mid + quicksort(more)  #把新的數列重整，把quicksort(less) 和quicksort(more)丟回去，若有兩個以上的數字，再重複上述步驟(選pivot、調整數列)
                                                                          #直到所有list中都只剩下一個數，分不出「新的數列」為止，就會停止分類
```


```python

```
