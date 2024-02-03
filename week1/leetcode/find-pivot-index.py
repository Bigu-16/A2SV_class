class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0]*(len(nums)+1)
        suff = [0]*(len(pref))

        for i in range(len(nums)):
            pref[i+1] = pref[i] + nums[i]

        for i in range(len(nums)-1,-1,-1):
            suff[i-1] = suff[i] + nums[i]
        
        for i in range(len(nums)):
            if pref[i] == suff[i]:
                return i

        return -1 