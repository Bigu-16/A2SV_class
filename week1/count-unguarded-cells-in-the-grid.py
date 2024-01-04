class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        row = m
        col = n

        grid = [[""]*col for _ in range(row)]

        covered_list = []

        for i,j in guards:
            grid[i][j] = "G"

        for i,j in walls:
            grid[i][j] = "W"

        for r,c in guards:
            currC = c
            while currC < n-1:
                if grid[r][currC+1] == "W" or grid[r][currC+1] == "G":
                    break
                grid[r][currC+1] = "*"
                currC += 1
            currC = c
            while currC > 0:
                if grid[r][currC-1] == "W" or grid[r][currC-1] == "G":
                    break
                grid[r][currC-1] = "*"
                currC -= 1
            currR = r
            while currR < m-1:
                if grid[currR+1][c] == "W" or grid[currR+1][c] == "G":
                    break
                grid[currR+1][c] = "*"
                currR += 1
            currR = r
            while currR > 0:
                if grid[currR-1][c] == "W" or grid[currR-1][c] == "G":
                    break
                grid[currR-1][c] = "*"
                currR -= 1
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "":
                    count += 1
        
        return count