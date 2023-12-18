class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split()
        reversed_s = " ".join(s_list[::-1])

        return reversed_s
