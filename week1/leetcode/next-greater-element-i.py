class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_ = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                next_[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_[num] = -1
        
        result = []
        for num in nums1:
            result.append(next_[num])
        
        return result

            