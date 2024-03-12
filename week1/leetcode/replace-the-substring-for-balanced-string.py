class Solution:
    def balancedString(self, s: str) -> int:
        s_dict = defaultdict(int)
        n = len(s)//4

        for ch in s:
            s_dict[ch] += 1
        
        l = 0
        min_ = len(s)

        for r , ch in enumerate(s):
            s_dict[ch] -= 1

            while all(s_dict[char] <= n for char in 'QWER') and  l < len(s):
                min_ = min(min_, r - l + 1)
                s_dict[s[l]] += 1
                l += 1

        return min_
