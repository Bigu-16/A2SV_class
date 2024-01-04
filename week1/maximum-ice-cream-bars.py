class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        summ = 0

        for i in range(len(costs)):
            if summ + costs[i] <= coins:
                summ += costs[i]
                count += 1


        return count