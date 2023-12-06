class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_num = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                max_num = max(current,max_num)
                current = 0
                
        return max(current,max_num)
