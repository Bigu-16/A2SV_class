class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x :abs(x[0] - x[1]), reverse = True)
        b = len(costs)//2
        a = len(costs)//2
        total = 0

        for costA,costB in costs:
            if b == 0 or (a > 0 and costA <= costB):
                total += costA
                a -= 1
            else:
                total += costB
                b -= 1
        return total