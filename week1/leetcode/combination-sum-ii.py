class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        bucket = []

        def backtrack(i):
            if sum(bucket) == target:
                ans.append(bucket[::])
            
            if sum(bucket) > target or i >= len(candidates):
                return
            
            if sum(bucket) < target:
                bucket.append(candidates[i])
                backtrack(i+1)
                bucket.pop()
                while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                backtrack(i+1)
            
        backtrack(0)
        return ans