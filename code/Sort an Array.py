class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
      if len(nums) < 2:
          return nums
      else:
          pivot = nums[0]
          less = [i for i in nums[1:] if i <= pivot]
          more = [i for i in nums[1:] if i > pivot]
          return self.sortArray(less) + [pivot] + self.sortArray(more)
    

