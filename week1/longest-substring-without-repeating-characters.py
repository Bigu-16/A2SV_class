class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_count = defaultdict(int)
        l = 0
        count = 0
        max_c = 0

        for r in range(len(s)):
            s_count[s[r]] += 1
            

            while s_count[s[r]] > 1:
                s_count[s[l]] -= 1
                l += 1
                count -= 1

            count += 1
            max_c = max(max_c,count)
        return max_c