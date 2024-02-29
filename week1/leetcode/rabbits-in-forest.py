class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c_dict = defaultdict(int)
        total = 0
        ans = 0

        for i in range(len(answers)):
            c_dict[answers[i]] += 1
            
        for i in c_dict:
            ans = ceil(c_dict[i] / (i+1)) * (i+1)
            total += ans
        return total
