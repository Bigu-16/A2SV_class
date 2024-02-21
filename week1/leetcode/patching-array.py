class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] > n:
                break
            while nums[i]-1 > curr:
                curr += curr+1
                count += 1
            curr += nums[i]
        while n > curr:
            curr += curr+1
            count += 1
        return count