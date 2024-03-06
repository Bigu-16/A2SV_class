class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums) 

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid 
        return -1