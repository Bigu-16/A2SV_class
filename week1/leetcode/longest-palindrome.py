class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
        
        ans = 0
        odd = False
        for key, value in s_dict.items():
            if value % 2 == 0:
                ans += value
            else:
                ans += value-1
                value = value - 1
                odd = True
        if odd:
            ans += 1
        return ans
                
