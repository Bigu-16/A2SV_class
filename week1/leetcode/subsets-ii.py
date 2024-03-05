class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        bucket = []
        ans = []

        def backtrack(i):
            if i >= len(nums):
                ans.append(bucket[::])
                return

            bucket.append(nums[i])
            backtrack(i+1)
            bucket.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
            
        backtrack(0)
        return ans

        