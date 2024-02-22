class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = list(s)
        count = Counter(s)
        stack = []

        for i in range(len(s)):
            if s[i] not in stack:
                while stack and stack[-1] > s[i] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(s[i])
            count[s[i]] -= 1
        
        return ''.join(stack)