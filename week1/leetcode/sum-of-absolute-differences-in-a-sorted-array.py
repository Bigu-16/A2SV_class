class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] *(n+1)

        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        ans = []
        for i in range(n):
            right = n - i - 1
            left_sum = nums[i] * i
            right_sum = nums[i] * right
            ans.append((left_sum - pref[i]) + (pref[-1] - pref[i+1] - right_sum))
        return ans
