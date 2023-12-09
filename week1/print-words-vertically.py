class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        vertical = []

        for i in range(max_len):
            column = ""
            for word in words:
                if i < len(word):
                    column += word[i]
                else:
                    column += " "

            vertical.append(column.rstrip())

        return vertical 

        
