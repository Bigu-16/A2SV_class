class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r = len(strs)
        c = len(strs[0])
        grid = [list(string) for string in strs]
        count = 0

        for col in range(c):
            for row in range(r-1):
                if strs[row][col] > strs[row+1][col]:
                    count += 1
                    break

        return count 