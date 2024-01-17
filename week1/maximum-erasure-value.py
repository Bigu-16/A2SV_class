class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        l = 0
        summ = 0

        for r in range(len(nums)):
            nums_dict[nums[r]] += 1

            while nums_dict[nums[r]] > 1:
                nums_dict[nums[l]] -= 1
                l += 1
            
            summ = max(summ,sum(nums[l:r+1]))
       
        return summ
           