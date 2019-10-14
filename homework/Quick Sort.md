

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
```


```python
quicksort(list)
```




    [0, 1, 3, 4, 6, 8, 8, 9, 11, 16]




```python

```
