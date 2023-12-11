class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        sums = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum not in sums:
                        sums[index_sum] = []
                    sums[index_sum].append(list1[i])

        min_sum = min(sums.keys())
        min_sum_restaurants = sums[min_sum]

        return min_sum_restaurants
