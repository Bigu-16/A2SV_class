class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(n):
            summ = 0
            count = 1
            for i in range(len(weights)):
                if summ + weights[i] > n:
                    summ = weights[i]
                    count += 1
                else:
                    summ += weights[i]
            if count <= days:
                return True
            return False

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

