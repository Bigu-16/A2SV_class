class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []  
        ans = [-1] * len(nums)
        n = len(nums)

        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                ans[idx] = nums[i % n]
            if i < n:
                stack.append(i) 
        
        return ans