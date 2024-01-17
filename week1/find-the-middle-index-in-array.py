class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref = []
        summ = 0

        for i in range(len(nums)):
            pref.append(summ)
            summ += nums[i]
        pref.append(summ)

        for i in range(1,len(pref)):
            if pref[i-1] == pref[-1] - pref[i]:
                return i-1
        

        return -1
            