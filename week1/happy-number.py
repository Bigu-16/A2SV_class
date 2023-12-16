class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n!= 1:
            squares_sum = 0

            while n > 0:
                digit = n % 10
                squares_sum += digit ** 2
                n //= 10

            if squares_sum in visited:
                return False

            visited.add(squares_sum)
            n = squares_sum

        return True