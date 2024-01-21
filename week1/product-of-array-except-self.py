class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*(len(nums)+1)
        suff = [1]*(len(nums)+1)
        ans = []
        
        for i in range(len(nums)):
            pref[i+1] = nums[i] * pref[i]
        for i in range(len(nums)-1,-1,-1):
            suff[i] = nums[i] * suff[i+1]
        
        for i in range(len(nums)):
            ans.append(pref[i] * suff[i+1])
        
        return ans
