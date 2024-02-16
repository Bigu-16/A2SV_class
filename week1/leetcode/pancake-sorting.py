class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        n = len(arr)
        while n > 1:
            max_index = arr.index(max(arr[:n]))

            if max_index != n - 1:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                result.append(max_index + 1)

                arr[:n] = reversed(arr[:n])
                result.append(n)

            n -= 1

        return result
