class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans_dict = {'T': 0, 'F': 0}
        l = 0
        max_num = 0
        
        for r in range(len(answerKey)):
            ans_dict[answerKey[r]] += 1
            max_num = max(max_num, ans_dict[answerKey[r]])

            if r - l + 1 - max_num > k:
                ans_dict[answerKey[l]] -= 1
                l += 1

        return len(answerKey) - l
