class Solution:
    def sortSentence(self, s: str) -> str:
        sent_list = list(s.split())
        sent_dict = defaultdict(int)
        ans = ""


        for string in sent_list:
            sent_dict[int(string[-1])] = string[:-1]
        sorted_dict = sorted(sent_dict)
        print(sorted_dict)

        for key in sorted_dict:
            ans += sent_dict[key] + " "

        return ans[:-1]
