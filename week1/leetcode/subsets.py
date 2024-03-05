class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def backtrack(i):
            if i == n:
                ans.append(path[:])
                return
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            backtrack(i + 1)
        backtrack(0)
        return ans