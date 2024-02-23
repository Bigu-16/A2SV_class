class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            for j in range(i+1,len(nums)-1):
                val = nums[i] + nums[j] 
                k = bisect_left(nums,val)
                ans += k-j -1
    
        return ans 
