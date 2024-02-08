class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1') 
        total_zeroes = 0 
        max_score = 0 
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                total_zeroes += 1  
            current_score = total_zeroes + total_ones - (i + 1 - total_zeroes)
            max_score = max(max_score, current_score)
        
        return max_score
