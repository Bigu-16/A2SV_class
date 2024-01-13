class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        
        cnt = 0       

        if k == 1:
            for i in range(len(s)):
                if s[i] in vowel:
                    cnt += 1
                    return cnt

        else:
            curr_s = s[:k]
            for i in range(len(curr_s)):
                if curr_s[i] in vowel:
                    cnt += 1
            l = 1
            max_cnt = cnt

            for r in range(k,len(s)):
                if s[r] in vowel: 
                    cnt += 1  
                if s[l-1] in vowel:
                    cnt -= 1
                l += 1
                max_cnt = max(max_cnt,cnt)
                
            return max_cnt

    
        