class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        ans = float('inf')

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                ans = min(r - l + 1, ans)
                summ -= nums[l]
                l += 1

        if ans == float('inf'):
            return 0
        else:
            return ans
                