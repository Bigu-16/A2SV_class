class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_ = 0
        
        row = [0] * len(grid)
        col = [0] * len(grid[0])
        for r in range(len(grid)):  
            for c in range(len(grid[0])):
                col[c] = max(col[c], grid[r][c])
                row[r] = max(row[r], grid[r][c])
        for r in range(len(grid)):  
            for c in range(len(grid[0])):
                min_ = min(col[c], row[r])
                max_ += (min_ - grid[r][c])

        return max_