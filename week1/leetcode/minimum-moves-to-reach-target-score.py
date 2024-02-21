class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = target
        move = 0
        while n > 1:
            if not maxDoubles:
                move += n - 1
                n -= move
            else: 
                if n % 2 == 0:
                    n //= 2
                    maxDoubles -= 1
                    move += 1
                else:
                    n -= 1
                    move += 1
                
        return move