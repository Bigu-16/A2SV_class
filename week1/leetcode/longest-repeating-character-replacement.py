class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)

        left = 0
        count = 0 
        ans = 0
        for right in range(len(s)):
            s_dict[s[right]] += 1

            freq = max(s_dict.values())
            while (right - left + 1) - freq > k and left < len(s):  
                s_dict[s[left]] -= 1
                left += 1
            
            ans =  max(ans,right - left + 1)
        return ans