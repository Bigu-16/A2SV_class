class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        summ = 0
        left = 0
        right = len(piles)-2


        while left < right:
            if left <= len(piles)//3:
                summ += piles[right]
                right -= 2
                left += 1
                
        return summ
