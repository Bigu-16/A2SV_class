class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt_0 = 0
        l = 0
        max_sub = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt_0 += 1
                if cnt_0 > 1:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                    cnt_0 -= 1
            max_sub = max(max_sub,r-l)

        return max_sub
                    
        
                
