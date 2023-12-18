class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num-1 in nums_set:
                continue
            current_consecutive = 1
            while (num + current_consecutive) in nums_set:
                current_consecutive += 1
        
            longest = max(longest,current_consecutive)
        return longest

