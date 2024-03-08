class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums_dict = {0:-1}
        mod = sum(nums) % p
        curr_sum = 0
        min_ = len(nums)

        if mod == 0:
            return 0

        for i in range(len(nums)):
            curr_sum = (curr_sum + nums[i]) % p
            diff = (curr_sum - mod) % p

            if diff in nums_dict:
                min_ = min(min_,i - nums_dict[diff])
            nums_dict[curr_sum] = i
        return min_ if min_ < len(nums) else -1