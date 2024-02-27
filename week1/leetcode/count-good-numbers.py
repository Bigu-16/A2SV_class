class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9) + 7
        
        if n == 1:
            return 5
        if n == 2:
            return 20
    
        if n % 2 != 0:
            half = self.countGoodNumbers(n//2)  
            if (n//2) % 2 == 0:
                return 5 * half * half % mod
            else:
                return 4 * half * half % mod
        else:
            if (n//2) % 2:
                half = self.countGoodNumbers((n-2)//2)
                return 20 * half * half % mod
            half = self.countGoodNumbers(n//2)
            return half * half % mod
            