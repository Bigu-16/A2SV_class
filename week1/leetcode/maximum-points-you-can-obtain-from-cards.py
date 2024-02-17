class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        min_len = len(cardPoints) - k
        l, total, curr = 0, 0, 0
        min_sum = float('inf') 

        for r in range(len(cardPoints)):
            total += cardPoints[r]
            curr += cardPoints[r]

            if r - l + 1 == min_len:
                min_sum = min(min_sum, curr)
                curr -= cardPoints[l]
                l += 1

        if min_sum != float('inf'):
            return total - min_sum  
        else:
            return total
