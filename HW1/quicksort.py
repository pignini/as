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
