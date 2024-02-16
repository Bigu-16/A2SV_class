class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        min_ = float('inf')
        white = 0

        for r in range(len(blocks)):
            curr = blocks[r]
            if curr == "W":
                white += 1
                
            while r - l + 1 > k:
                l_chr = blocks[l]
                if l_chr == "W":
                    white -= 1
                l += 1
            
            if r - l + 1 == k:
                min_ = min(min_, white)

        return min_  
        
