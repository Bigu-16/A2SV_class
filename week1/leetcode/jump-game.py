class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        
        for n in range(len(nums)-1):
            curr = max(curr-1,nums[n])
            if curr == 0:
                return False
        return True