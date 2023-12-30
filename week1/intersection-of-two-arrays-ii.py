class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        inter_set = set(nums1).intersection(set(nums2))

        inter_set = list(inter_set)
        ans = []
        for num in inter_set:
            ans = ans + ([num] * min(nums1[num],nums2[num]))
        return ans