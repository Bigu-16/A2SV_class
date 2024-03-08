class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_val = 0
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            max_val = max(max_val, ceil(summ / (i + 1)))

        return max_val

       
