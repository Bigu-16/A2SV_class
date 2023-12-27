class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        summ = 0

        for r in range(row):
            for c in range(col):
                if r-c == 0 or r+c == col-1:
                    summ += mat[r][c]

        return summ
