class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_num = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]!=nums[i-1]:
                nums[next_num] = nums[i]
                next_num += 1
        
        return next_num