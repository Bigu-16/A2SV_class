class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        start_pt = [0,0]

        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= abs(start_pt[0] + target[0]) + abs(start_pt[1] + target[1]):
                return False
        return True
