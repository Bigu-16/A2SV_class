class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0 
        left = 0
        right = 0
        freq_dict = defaultdict(int)
        ele = len(set(nums))

        while right < len(nums):
            if nums[right] not in freq_dict:
                freq_dict[nums[right]] = 0
            freq_dict[nums[right]] += 1

            while len(freq_dict) == ele:
                count += len(nums) - right

                freq_dict[nums[left]] -= 1
                if freq_dict[nums[left]] == 0:
                    del freq_dict[nums[left]]
                left += 1
            right += 1
        return count 