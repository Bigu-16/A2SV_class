class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # bubble
        n = len(heights)
        m = len(heights)
        for i in range(n):
            for j in range(m-1):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1], heights[j]
                    names[j],names[j+1] = names[j+1], names[j]
            m -= 1
        return names

        # selection
        # for n in range(1,len(names)):
        #     for h in range(1,len(heights)):
        #         if heights[h-1] > heights[h]:
        #             height
