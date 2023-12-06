class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(1,len(nums)):
            if i % 2 == 1:
                decompressed += [nums[i]]*nums[i-1]
        return decompressed