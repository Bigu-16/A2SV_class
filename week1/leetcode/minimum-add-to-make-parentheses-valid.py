class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        l = 0
        move = 0

        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                if l:
                    l -= 1
                else:
                    move += 1
        if l:
            move += l
        return move