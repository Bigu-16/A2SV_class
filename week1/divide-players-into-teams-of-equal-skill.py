class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        pair = []
        summ = skill[left] + skill[right]
        curr_sum = 0

        while left < right:
            curr_sum = skill[left] + skill[right]
            if curr_sum != summ:
                return -1
            else:
                pair.append(skill[left]*skill[right])
                left += 1
                right -= 1

        ans = sum(pair)
        return ans
        

