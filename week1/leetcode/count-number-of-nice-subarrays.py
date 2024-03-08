class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref = [0]*(len(nums)+1)

        for i in range(len(nums)):
            pref[i+1] = pref[i] + (nums[i] % 2)

        left = 0
        count = 0
        prev = 0
        for i in range(len(pref)):
            if prev and pref[i] == pref[i-1]:
                count += prev
            else:
                prev = 0
                while pref[i] - pref[left] >= k:
                    if pref[i] - pref[left] == k:
                        prev += 1
                    left += 1
                count += prev
        return count