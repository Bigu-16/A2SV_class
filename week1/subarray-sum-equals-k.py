class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_dict = defaultdict(int)
        pref = [0]*(len(nums)+1)

        for i in range(len(nums)):
            pref[i+1] = nums[i] + pref[i]

        ans = 0

        for i in range(1,len(pref)):
            if pref[i] == k:
                ans += 1
            n = pref[i] - k
            if n in nums_dict:
                ans += nums_dict[n]
            nums_dict[pref[i]] += 1

        return ans
        

        
