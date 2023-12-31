class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        num = 0

        for i in range(len(flips)):
            num = max(num,flips[i])
            if i+1 == num:
                count += 1

        return count

        