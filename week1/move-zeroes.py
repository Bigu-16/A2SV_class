class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seek = 0 
        hold = 0

        while seek < len(nums):
            if nums[seek] != 0:
                nums[hold], nums[seek] = nums[seek],nums[hold]
                hold += 1
            seek += 1
             