class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {}

        for keys,values in enumerate(nums):
            nums_dict[values] = keys

        for i,k in operations:
            nums[nums_dict[i]] = k
            nums_dict[k]=nums_dict.pop(i)

        return nums
            