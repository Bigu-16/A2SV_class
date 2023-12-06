class Solution:
    def totalMoney(self, n: int) -> int:
        num = 0
        summ = 0

        for i in range(n):
            summ+= ((i//7)+(i%7)+1)
        return summ