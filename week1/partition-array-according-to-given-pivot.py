class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums_less = []
        nums_greater = []
        pivot_num = []
        relative_order = []

        for i in nums:
            if i < pivot:
                nums_less.append(i)
            elif i == pivot:
                pivot_num.append(i)
            elif i > pivot:
                nums_greater.append(i)

        relative_order = nums_less + pivot_num + nums_greater

        return relative_order

