class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        for i in range(0, len(s), 2 * k):
            list_s[i:i+k] = reversed(list_s[i:i+k])
            # if len(s) - i < k:
            #     list_s[i:] = reversed(list_s[i:])
                
            # if 2 * k >= len(s) - i >= k:
            #     list_s[i:i+k] = reversed(list_s[i:i+k])

        return "".join(list_s)