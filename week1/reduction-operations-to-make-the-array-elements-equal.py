class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        set_nums = set(nums)
        set_nums = sorted(set_nums)

        set_dict = {}
        for i,num in enumerate(set_nums):
            set_dict[num] = i

        count = 0
        for i in range(len(nums)):
            count += set_dict[nums[i]]
        
        return count
