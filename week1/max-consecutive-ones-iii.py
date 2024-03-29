class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        cnt_zero = 0
        max_one = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt_zero += 1
            
            while cnt_zero > k:
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1
            
            max_one = max(max_one, right - left + 1)

        return max_one
