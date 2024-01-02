class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        # print(nums[1],nums[0] = nums[0],nums[1])
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i],nums[j] = nums[j],nums[i]
        if nums[0] == "0":
            return "0"

        ans = ''
        for i in range(len(nums)):
            ans += nums[i] 
        return ans
