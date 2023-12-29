class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_num = max(nums)
        arr = [0]*(max_num + 1)
        ans = [0]*len(nums)
        for num in nums:
            arr[num] += 1
        for i in range(len(nums)):
            ans[i] = sum(arr[:nums[i]])
        return ans

