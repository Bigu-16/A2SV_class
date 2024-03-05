class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        bucket = []
        ans = []
        def backtrack(i):
            if len(bucket) == k and sum(bucket) == n:
                ans.append(bucket[:])
                return 

            if sum(bucket) > n:
                return
            
            for j in range(i+1,10):
                bucket.append(j)
                backtrack(j)
                bucket.pop()

        backtrack(0)
        return ans
