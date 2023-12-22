class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for r in range(row-2):
            
            for c in range(col-2):
                summ = sum(grid[r][c:c+3]) + sum(grid[r+2][c:c+3]) + grid[r+1][c+1]
                ans = max(summ,ans)
        return ans