class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = nums[0]
        max_ = nums[0]

        for i in range(1,len(nums)):
            summ = max(summ + nums[i], nums[i])
            max_ = max(max_,summ)

        return max_
