class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        s = list(s)

        for i in range(len(s)):
            if s[i] == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)