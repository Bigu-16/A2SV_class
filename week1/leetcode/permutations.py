class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        bucket = []
        ans = []

        def backtrack(i):
            if len(bucket) == len(nums):
                ans.append(bucket[::])
                return

            for j in range(len(nums)):
                if nums[j] not in bucket:
                    bucket.append(nums[j])
                    backtrack(j)
                    bucket.pop()

        backtrack(0)
        return ans

