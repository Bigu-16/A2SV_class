class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        rearranged = []

        for i in nums:
            if i > 0:
                positive.append(i)
                
            elif i < 0:
                negative.append(i)

        for n in range(len(positive) ):
            rearranged.append(positive[n])
            rearranged.append(negative[n])

        return rearranged

     