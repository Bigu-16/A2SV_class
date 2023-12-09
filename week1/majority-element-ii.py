class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        elements = []

        for element,count in Counter(nums).items():
            if count > n//3:
                elements.append(element)

        return elements
