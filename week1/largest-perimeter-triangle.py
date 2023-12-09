class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for i in range(len(nums)-2):
            side1 = nums[i]
            side2 = nums[i+1]
            side3 = nums[i+2]

            if side1 < side2 + side3:
                return side1 + side2 + side3
               
        return 0