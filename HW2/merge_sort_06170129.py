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
