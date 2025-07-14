class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1        



#2 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l_t = 0
        for i in range(len(nums)):
           r_t = t - l_t - nums[i]
           if r_t == l_t:
               return i
           l_t += nums[i]
        return -1         
