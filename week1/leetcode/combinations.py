class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        bucket = []
        ans = []
        def backtrack(num):
            if len(bucket) == k:
                ans.append(bucket[::])
                return 
            
            for j in range(num+1,n+1):
                bucket.append(j)
                backtrack(j)
                bucket.pop()

        backtrack(0)
        return ans
        
                