class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        greatest_among = []

        for i in range(len(candies)):
            if extraCandies + candies[i] >= max_candy:
                greatest_among.append(True)
            else:
                greatest_among.append(False)
        return greatest_among
        