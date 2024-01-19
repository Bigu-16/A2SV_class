class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        pref = [0]*(len(s)+1)

        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                pref[shifts[i][0]] += 1
                if shifts[i][1] + 1 < len(pref):
                    pref[shifts[i][1] + 1] -= 1
            else:
                pref[shifts[i][0]] -= 1
                if shifts[i][1] + 1 < len(pref):
                    pref[shifts[i][1] + 1] += 1

        ans = ""
        p = 0
        for i in range(len(s)):
            p += pref[i]
            p %= 26
            ans += chr((ord(s[i]) - ord('a') + p + 26) % 26 + ord('a'))

        return ans

