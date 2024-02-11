class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ = float('inf')

        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(summ - target):
                    summ = total
            
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  
                
        return summ