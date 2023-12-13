class Solution:
    def missingNumber(self, nums: List[int]) -> int:
 
        num = list(set(range(0, len(nums) + 1)) - set(nums))

        return num[0]

