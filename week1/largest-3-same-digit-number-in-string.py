class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for number in range(9,-1,-1):
            maximum = str(number) * 3
            if maximum in num:
                return maximum
        return ""