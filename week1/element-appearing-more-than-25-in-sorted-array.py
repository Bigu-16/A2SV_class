class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        
        for i, count in Counter(arr).items():
            if count > n:
                return i
