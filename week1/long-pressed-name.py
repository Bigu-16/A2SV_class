class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False

            count_name = 1
            while i + 1 < len(name) and name[i] == name[i + 1]:
                i += 1
                count_name += 1

            count_typed = 1
            while j + 1 < len(typed) and typed[j] == typed[j + 1]:
                j += 1
                count_typed += 1

            if count_typed < count_name:
                return False

            i += 1
            j += 1

        return i == len(name) and j == len(typed)
