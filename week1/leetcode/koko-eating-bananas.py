class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(num):
            checked = 0
            for p in piles:
                checked += ceil(p/num)
            
            if checked <= h:
                return True
            return False
       
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left