class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        ans = 0

        while left < right:
            while left < right and s[left] == "0":
                left += 1
            while left < right and s[right] == "1":
                right -= 1
            ans += right - left
            left += 1
            right -= 1
        return ans

