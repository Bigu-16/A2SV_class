class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0

        if numOnes >= k:
            ans = k
        elif numOnes + numZeros < k:
            dif = k - (numOnes + numZeros)
            ans = numOnes - dif
        elif numOnes + numZeros >= k:
            ans = numOnes 
            
        return ans