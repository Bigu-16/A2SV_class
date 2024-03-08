class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_dict = defaultdict(int)
        max_ = 0
        l = 0

        for r in range(len(fruits)):
            fruits_dict[fruits[r]] += 1

            while len(fruits_dict) > 2:
                fruits_dict[fruits[l]] -= 1
                if fruits_dict[fruits[l]] == 0:
                    del fruits_dict[fruits[l]] 
                l += 1
            max_ = max(max_,r-l + 1)
        
        return max_
                