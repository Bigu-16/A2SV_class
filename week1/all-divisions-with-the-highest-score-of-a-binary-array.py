class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_1 = nums.count(1)
        count_0 = 0

        nums_dict = {}

        nums_dict[0] = count_1

        for i, value in enumerate(nums):
            if value == 0:
                count_0 += 1
            else:
                count_1 -= 1
            
            nums_dict[i+1] = count_1 + count_0 
        max_val = max(nums_dict.values())

        ans = []
        for key, value in nums_dict.items():
            if max_val == value:
                ans.append(key)

        return ans
