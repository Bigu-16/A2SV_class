class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        element = 0

        for num , count in Counter(nums).items():
            if count > n/2:
                element = num
                return element
