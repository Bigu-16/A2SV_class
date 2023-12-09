class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        written = []
        word = ""

        for each_word in words:
            word = set(each_word.lower())
            if word.issubset(row1) or word.issubset(row2) or word.issubset(row3):
                written.append(each_word)

        return written 
