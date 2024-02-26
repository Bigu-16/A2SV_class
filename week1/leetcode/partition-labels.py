class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = i
        max_ = 0
        last = 0
        ans = []

        for i in range(len(s)):
            max_ = max(s_dict[s[i]], max_)
            if max_ == i:
                ans.append(max_ - last + 1)
                last = max_ + 1
        return ans
