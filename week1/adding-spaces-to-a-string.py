class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str_list = []
        new_string = ""

        for idx in range(len(spaces)):
            if idx == 0:
                new_str_list.append(s[:spaces[idx]])
            else:
                new_str_list.append(s[spaces[idx-1]:spaces[idx]])
        
        new_str_list.append(s[spaces[-1]:])
        new_str_list = " ".join(new_str_list)
        return new_str_list
