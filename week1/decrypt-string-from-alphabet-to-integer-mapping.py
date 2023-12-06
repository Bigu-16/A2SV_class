class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1 
        num = 0
        string = ""

        while i >= 0:
            if s[i] == "#":
                num = int(s[i-2] + s[i-1])
                string += chr(num + 96)
                i -= 3
            else:
                num = int(s[i])
                string += chr(num + 96)
                i -= 1
        string = string[ : :-1]

        return string





