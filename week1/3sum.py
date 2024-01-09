class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        ans = (tuple(a) for a in ans)
        ans  = list(set(ans))
        ans = [list(a) for a in ans]
        return ans
            

                