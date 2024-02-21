class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = list(palindrome)
        s = ''
        n = len(ans)//2

        for i in range(n):
            if ans[i] != 'a':
                ans[i] = 'a'
                return "".join(ans)
        if len(ans) > 1 and ans[-1] == 'a':
            ans[-1] = 'b'
            return "".join(ans)
        
        return s

        


