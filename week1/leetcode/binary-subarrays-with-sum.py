class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = [0]* (len(nums)+1)

        for i in range(len(nums)):
            pref[i+1] = pref[i] + nums[i]

        nums_dict = defaultdict(int)
        ans = 0
        
        for r in range(1,len(pref)):
            if pref[r] == goal:
                ans += 1
            dif = pref[r] - goal
            if dif in nums_dict:
                ans += nums_dict[dif]
            if pref[r] in nums_dict:
                nums_dict[pref[r]] += 1
            else:
                nums_dict[pref[r]] = 1

        return ans
