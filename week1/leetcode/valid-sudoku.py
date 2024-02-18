class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_subgrid = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    if num in seen_row[r] or num in seen_col[c] or num in seen_subgrid[(r // 3) * 3 + (c // 3)]:
                        return False
                    seen_row[r].add(num)
                    seen_col[c].add(num)
                    seen_subgrid[(r // 3) * 3 + (c // 3)].add(num)

        return True
