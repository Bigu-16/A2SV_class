class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7

        freq = [0] * len(nums)
        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(freq):
                freq[end + 1] -= 1

        for i in range(1,len(freq)):
            freq[i] += freq[i-1]
        
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        max_ = 0
        for i in range(len(freq)):
            max_ += freq[i] * nums[i]
            max_ %= mod
        
        return max_