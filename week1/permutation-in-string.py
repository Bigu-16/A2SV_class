class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        if len(s1) > len(s2):
            return False

        curr_dict = defaultdict(int)
        for i in s2[:len(s1)]:
            curr_dict[i] += 1

        if Counter(s1) == Counter(curr_dict):
            return True

        l = 1
        curr_s2 = defaultdict(int)
        for i in s2[:len(s1)]:
            curr_s2[i] += 1

        for r in range(len(s1), len(s2)):
            curr_s2[s2[l-1]] -= 1
            curr_s2[s2[r]] += 1

            if Counter(s1) == Counter(curr_s2):
                return True

            l += 1

        return False
