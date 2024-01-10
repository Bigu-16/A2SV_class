class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        l = 0
        ans = []

        if p_count == s_count:
            ans.append(l)

        for r in range(len(p),len(s)):
            s_count[s[l]] -= 1
            
            s_count[s[r]] += 1

            if s_count[s[l]] == 0:
                del s_count[s[l]]
            l += 1

            if s_count == p_count:
                ans.append(l)
        return ans








