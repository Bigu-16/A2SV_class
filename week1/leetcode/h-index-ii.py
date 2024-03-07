class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1

        ans = 0
        while left <= right:
            mid = (left + right) // 2

            diff = len(citations) - mid
            if citations[mid] >= diff:
                ans = diff
                right = mid - 1
            else:
                left = mid + 1
        return ans