class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)
        isFound = False
        ans = []

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                isFound = True
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if isFound:
            ans.append(right)
        else:
            ans.append(-1)

        left = right -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if isFound:
            ans.append(left)
        else:
            ans.append(-1)
        return ans