class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = []

        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    index_nums.append(i)
                    index_nums.append(j)
                    
                    return index_nums

        return index_nums