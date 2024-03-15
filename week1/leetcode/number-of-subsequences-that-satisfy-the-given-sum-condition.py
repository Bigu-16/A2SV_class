class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = (10 ** 9) + 7
        def find(nums,diff):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                
                if nums[mid] <= diff:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        ans = 0
        for i in range(len(nums)):
            diff = abs(target - nums[i])

            num = find(nums,diff)

            if num >= i:
                ans += 2 ** (num - i)
            
        
        return ans % mod