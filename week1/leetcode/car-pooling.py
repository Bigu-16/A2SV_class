class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0] * 1001

        for num, from_, to in trips:
            pref[from_] += num
            pref[to] -= num

        for i in range(0, len(pref)):
            if i > 0:
                pref[i] += pref[i - 1]
            if pref[i] > capacity:
                return False
        return True