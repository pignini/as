
## HOMEWORK2      MERGE SORT 學習歷程＆流程圖
  
*  參考資料： https://www.geeksforgeeks.org/merge-sort/


```python
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
```


```python
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
```

    Given array is
    12 11 13 5 6 7 
    Sorted array is: 
    5 6 7 11 12 13 


以上是我從網路上查詢到的程式碼，跟heap sort一樣，決定先了解網路上的程式碼後自己再重新打過一遍。


```python
def merge(nums):
    i=0
    l=0
    r=0
    if  left[l]<right[r]:
        nums[i]= left[l]
        l=l+1
        i=i+1
    else:
        nums[i]= right[r]
        r=r+1
        i=i+1        
def merge_sort(nums): 
    n=len(nums)
    middle=n // 2   
    if n>1:
        left=nums[:middle]
        right=nums[middle:]
        merge(left) 
        merge(right)        
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-f269d9e2d6d6> in <module>
          1 nums = [12, 11, 6, 13, 5, 6, 7, 7]
    ----> 2 merge_sort(nums)
    

    <ipython-input-3-dc80223dce14> in merge_sort(nums)
         17         left=nums[:middle]
         18         right=nums[middle:]
    ---> 19         merge(left)
         20         merge(right)


    <ipython-input-3-dc80223dce14> in merge(nums)
          3     l=0
          4     r=0
    ----> 5     if  left[l]<right[r]:
          6         nums[i]= left[l]
          7         l=l+1


    NameError: name 'left' is not defined


第一次一定錯誤都很多，所以現在來一個一個找出來，因為跑這個程式碼的順序是要先看下面的def的那段，所以我先檢查那裡，我第一個發現的是middle=n // 2這段，我放的位置順序不太正確，應該是要先看n是否大於1，確定大於1後才能跑middle=n // 2這個程式碼。


```python
def merge(nums):
    i=0
    l=0
    r=0
    if  left[l]<right[r]:
            nums[i]= left[l]
            l=l+1
            i=i+1
    else:
            nums[i]= right[r]
            r=r+1
            i=i+1        
def merge_sort(nums):
    n=len(nums)
    if n>1:
        middle=n // 2   
        left=nums[:middle]
        right=nums[middle:]
        merge(left) 
        merge(right)  
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-f269d9e2d6d6> in <module>
          1 nums = [12, 11, 6, 13, 5, 6, 7, 7]
    ----> 2 merge_sort(nums)
    

    <ipython-input-5-482c47ea4a4d> in merge_sort(nums)
         17         left=nums[:middle]
         18         right=nums[middle:]
    ---> 19         merge(left)
         20         merge(right)


    <ipython-input-5-482c47ea4a4d> in merge(nums)
          3     l=0
          4     r=0
    ----> 5     if  left[l]<right[r]:
          6             nums[i]= left[l]
          7             l=l+1


    NameError: name 'left' is not defined


改完後還是有問題，所以我在繼續找上面的def，我一開始一直覺得這個程式碼沒有問題，還詢問了同學哪裡有問題，然後他跟我說我少設了一條規則，不能讓程式碼這樣跑，左邊的變數要少於左邊的數的長度才會有東西（數值）存在在裡面，右邊也一樣，而我沒有設定這條條件所以這樣會是錯誤的，所以我便設定了while l<len(left) and r<len(right):，在這裡解釋一下while迴圈，因為我有點小遺忘這個迴圈的用法
簡單來說while跟for的差別是：
* while：控制在一個條件成立  a = 0   while a < 3:   count += 1  print a -> 0,1,2 
          如果a小於3，才能跑這個迴圈
* for：控制在一個範圍之內   for i in range(0, 3 , 1):   print i -> 0,1,2 
         把i直接跑for迴圈
         
所以while l<len(left) and r<len(right): 的意思是，假如左邊的變數少於左邊的數的長度和右邊的變數少於右邊的數的長度，兩個同時成立時才能再跑下面的程式碼。        


```python
def merge(nums):
    i=0
    l=0
    r=0
    while l<len(left) and r<len(right): 
        if  left[l]<right[r]:
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1        
def merge_sort(nums):
    n=len(nums)
    if n>1:
        middle=n // 2   
        left=nums[:middle]
        right=nums[middle:]
        merge(left) 
        merge(right)  
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-f269d9e2d6d6> in <module>
          1 nums = [12, 11, 6, 13, 5, 6, 7, 7]
    ----> 2 merge_sort(nums)
    

    <ipython-input-7-219fb131883b> in merge_sort(nums)
         18         left=nums[:middle]
         19         right=nums[middle:]
    ---> 20         merge(left)
         21         merge(right)


    <ipython-input-7-219fb131883b> in merge(nums)
          3     l=0
          4     r=0
    ----> 5     while l<len(left) and r<len(right):
          6         if  left[l]<right[r]:
          7             nums[i]= left[l]


    NameError: name 'left' is not defined


好這邊還是錯的，所以我繼續往下看，我重新看了一下merge sort的定義跟結構，（這邊卡超久......），重新看了一些影片，終於意識到，會出現左邊的數值都丟完（或是右邊的數值都丟完），而右邊（左邊）卻還有數值的狀況，這時要把剩餘的數值丟進排列過後的數列，這邊不用再排序應該前面已經排好左右兩邊各自的數值，為了完成以上的程序所以寫了這個程式碼，我原本想用if寫，但後來想到我應該是要剛才的while迴圈整個跑完後再跑一個新的，而不是從第一個while迴圈裡面跑，所以我又設了一個while迴圈，左邊的變數要少於左邊的數的長度或是右邊的變數要少於右邊的數的長度，如果左邊的變數少於左邊的數的長度，把左邊後面的數值都丟進排列過後的數列，右邊以此類推，所以程式碼長以下這樣：
*   while l<len(left) or r<len(right):  
        if  l<len(left):
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1 


```python
def merge(nums):
    i=0
    l=0
    r=0
    while l<len(left) and r<len(right): 
        if  left[l]<right[r]:
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1   
    while l<len(left) or r<len(right):  
        if  l<len(left):
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1 
def merge_sort(nums):
    n=len(nums)
    if n>1:
        middle=n // 2   
        left=nums[:middle]
        right=nums[middle:]
        merge(left) 
        merge(right)  
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-f269d9e2d6d6> in <module>
          1 nums = [12, 11, 6, 13, 5, 6, 7, 7]
    ----> 2 merge_sort(nums)
    

    <ipython-input-9-061d16df5f44> in merge_sort(nums)
         27         left=nums[:middle]
         28         right=nums[middle:]
    ---> 29         merge(left)
         30         merge(right)


    <ipython-input-9-061d16df5f44> in merge(nums)
          3     l=0
          4     r=0
    ----> 5     while l<len(left) and r<len(right):
          6         if  left[l]<right[r]:
          7             nums[i]= left[l]


    NameError: name 'left' is not defined


恩很棒還是錯的：）），我想了一下看到了merge(left)和merge(right)，我想試試看把兩個合在一起丟上去，看看會不會是對的，所以我改成merge(nums,left,right)，然後def merge(nums):改成def merge(nums,left,right): 


```python
def merge(nums,left,right): 
    i=0
    l=0
    r=0
    while l<len(left) and r<len(right): 
        if  left[l]<right[r]:
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1       
    while l<len(left) or r<len(right):  
        if  l<len(left):
            nums[i]= left[l]
            l=l+1
            i=i+1
        else:
            nums[i]= right[r]
            r=r+1
            i=i+1 
def merge_sort(nums):
    n=len(nums)  
    if n>1:
        middle=n // 2 
        left=nums[:middle]
        right=nums[middle:]
        merge(nums,left,right)   
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


```python
nums
```




    [5, 6, 7, 7, 12, 11, 6, 13]



好我不知道這樣算不算是好的開始，但是至少他跑出東西了，雖然還是錯的.......，好看來我得整個重新思考......。我認為我改成merge(nums,left,right)這個部分沒有錯， 然後我就發現到了，我應該把左邊跟右邊都先丟回merge_sort才對，丟完後兩邊在丟到merge，所以我改成：
*  def merge_sort(nums):
        n = len(nums)
        if n > 1:
        middle = n // 2
        left = nums[:middle]
        right = nums[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(nums,left,right)


```python
def merge(nums,left,right):
    i = 0
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            nums[i] = left[l]
            l = l + 1
            i = i + 1
        else:
            nums[i] = right[r]
            r = r + 1
            i = i + 1
    while l < len(left):
        nums[i] = left[l]
        l = l + 1
        i = i + 1

    while r < len(right):
        nums[i] = right[r]
        r = r + 1
        i = i + 1

def merge_sort(nums):
    n = len(nums)
    if n > 1:
        middle = n // 2
        left = nums[:middle]
        right = nums[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(nums,left,right)
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```


```python
nums
```




    [5, 6, 6, 7, 7, 11, 12, 13]



只能說謝謝我要哭了，看到答案的當下真的泛淚，我的天跑了In[518]次......。

# 解釋整個程式碼：


```python
##先解釋這段  

def merge_sort(nums):       # nums為隨便的數列
    n=len(nums)                 # n=隨便的數列的長度
    if n>1:                         # 假如n大於1，跑下列的程式碼
        middle=n // 2          # 把數列的長度除以2，//的意思是假如除以2後不是整數他會取成整數，設為middle這個變數
        left=nums[:middle]    # 把nums從最一開始到middle的數設為left
        right=nums[middle:]  # 把nums從middle到最後的數設為right
        merge_sort(left) 
        merge_sort(right)      # 把right和left丟進merge_sort
        merge(nums,left,right) #丟到merge變數
    ##這邊是先拆解數列，讓我們列出分裂的數列  
        
##再來是:

def merge(nums,left,right):           #定義merge
        i=0
        l=0
        r=0                                     #設定三個變數i,l,r，都設為1
    while l<len(left) and r<len(right):     #while迴圈我上面有介紹過，假如l小於left的長度和r小於right的長度，都符合才能跑下列的程式碼
         if  left[l]<right[r]:                     #以第一次跑來講，如果左邊的第一個數小於右邊的第一個數，跑下列的程式碼
            nums[i]= left[l]                     #排序後的數列的第一個數就應該放左邊的第一個數
            l=l+1                                   
            i=i+1                                   #然後就要把l跟i都加一個數，因為要比下一個數字，且丟到排序後的數列的下一個位置
        else:                                       #其他的，也就是如果左邊的第一個數大於等於右邊的第一個數
            nums[i]= right[r]                   #排序後的數列的i位置就應該放右邊的r位置的數               
            r=r+1
            i=i+1                                   #然後就要把r跟i都加一個數，因為要比下一個數字，且丟到排序後的數列的下一個位置       
     ##這邊是開始組合比較過後的數列的第一部份
    
##最後是：

    while l<len(left) or r<len(right):   #假如l小於left的長度或是r小於right的長度，符合一項才能跑下列的程式碼，上面有介紹過為什麼有這段程式碼
                                             #假如左邊的數值都丟完（或是右邊），而右邊（左邊）卻還有數值，這時要把剩餘的數值丟進排列過後的數列
        if  l<len(left):                       #如果l小於left的長度，跑下列的程式碼
            nums[i]= left[l]                #排序後的數列的i位置就應該放左邊的l位置的數 
            l=l+1
            i=i+1                              #然後就要把l跟i都加一個數，因為要比下一個數字，且丟到排序後的數列的下一個位置
        else:                                  #其他的，也就是如果r小於right的長度
            nums[i]= right[r]              #排序後的數列的i位置就應該放右邊的r位置的數    
            r=r+1
            i=i+1                              #然後就要把r跟i都加一個數，因為要比下一個數字，且丟到排序後的數列的下一個位置       
    ##這邊是組合比較過後的數列的第二部份，跑出最後的排列結果
```

在這邊我重新比對了一下，我會後的結果跟網路上找到的其實幾乎一樣了，最大的差別應該是網路上的是設成兩個while迴圈：
* while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1        
   while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
而我是設成用一個while迴圈跑，再加上用if else：
* while l<len(left) or r<len(right):  
       if  l<len(left):
           nums[i]= left[l]
           l=l+1
           i=i+1
       else:
           nums[i]= right[r]
           r=r+1
           i=i+1 
           
還有我設成兩個def，原本是一個而已：
* def merge_sort(nums): 跟 def merge(nums,left,right): 

再來加上return


```python
def merge(nums,left,right):
    i = 0
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            nums[i] = left[l]
            l = l + 1
            i = i + 1
        else:
            nums[i] = right[r]
            r = r + 1
            i = i + 1
    while l < len(left):
        nums[i] = left[l]
        l = l + 1
        i = i + 1

    while r < len(right):
        nums[i] = right[r]
        r = r + 1
        i = i + 1


def merge_sort(nums):
    n = len(nums)
    if n > 1:
        middle = n // 2
        left = nums[:middle]
        right = nums[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(nums,left,right)
    return nums
```


```python
nums = [12, 11, 6, 13, 5, 6, 7, 7] 
merge_sort(nums)
```




    [5, 6, 6, 7, 7, 11, 12, 13]



# 改成助教的格式


```python
class Solution(object):
    def merge_sort(self, nums):
        n = len(nums)
        if n > 1:
            middle = n // 2
            left = nums[:middle]
            right = nums[middle:]
            self.merge_sort(left)
            self.merge_sort(right)
            self.merge(nums,left,right)
        return nums
    def merge(self,nums,left,right):
        i = 0
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[i] = left[l]
                l = l + 1
                i = i + 1
            else:
                nums[i] = right[r]
                r = r + 1
                i = i + 1
        while l < len(left):
            nums[i] = left[l]
            l = l + 1
            i = i + 1   
        while r < len(right):
            nums[i] = right[r]
            r = r + 1
            i = i + 1
```


```python
a=[8,3,5,1,0,-3,4]
Solution().merge_sort(a)
```




    [-3, 0, 1, 3, 4, 5, 8]




```python

```

# 流程圖
 ![](/image/merge%20sort流程圖.jpg)
