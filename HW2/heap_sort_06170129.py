class Solution(object):
    def heap_sort(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0) 
        return nums
                  
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
