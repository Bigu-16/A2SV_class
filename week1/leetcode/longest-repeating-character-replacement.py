class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)

        left = 0
        ans = 0
        max_count = 0
        for right in range(len(s)):
            s_dict[s[right]] += 1

            max_count = max(max_count,s_dict[s[right]])
            while (right - left + 1) - max_count > k:  
                s_dict[s[left]] -= 1
                left += 1
            
            ans =  max(ans,right - left + 1)
        return ans