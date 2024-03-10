class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(list)

        for i, num in enumerate(nums):
            nums_dict[num].append(i)

        ans = [0] * len(nums)
        for num in nums_dict:
            index = nums_dict[num]
            pref = [0]
            for idx in index:
                pref.append(pref[-1] + idx)
            for i, idx in enumerate(index):
                left = idx * (i + 1) - pref[i + 1]
                right = pref[-1] - pref[i] - idx * (len(index) - i)
                ans[idx] = left + right
            
        return ans