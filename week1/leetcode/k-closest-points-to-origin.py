class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for i, j in points:
            summ = (i ** 2) + (j ** 2)
            dist.append([summ, i, j])

        dist.sort()

        ans = [point[1:] for point in dist[:k]]

        return ans
