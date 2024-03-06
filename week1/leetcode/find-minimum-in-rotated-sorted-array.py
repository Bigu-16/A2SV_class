class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1 
        # min_ = 

        while left <= right:
            mid = (left + right) // 2

            if left == right:
                return nums[mid]

            if nums[mid] > nums[right] or nums[mid] < nums[left]:
                left = mid 
            if nums[mid] < nums[right]:
                right = mid 
        return left
