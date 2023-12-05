class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = map(int,nums)
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums [j] and i<j:
                    count += 1
        return count 
