class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(num):
            div = 0
            ans = []
            for i in range(len(nums)):
                div = ceil(nums[i]/num)
                ans.append(div)
            
            summ = sum(ans)
            if summ <= threshold:
                return True
            return False

        left = 1
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

