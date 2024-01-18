class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def lessThanK(p):
            nums_dict = defaultdict(int)
            l = 0
            good = 0
            for r in range(len(nums)):
                nums_dict[nums[r]] += 1

                while len(nums_dict) > p:
                    nums_dict[nums[l]] -= 1
                    if nums_dict[nums[l]] == 0:
                        del nums_dict[nums[l]]

                    l += 1
                good += (r-l+1)
            return good

        return lessThanK(k) - lessThanK(k-1)
        


        # for r in range(len(nums)):
        #     nums_dict[nums[r]] += 1

        #     if len(nums_dict) == k and r > 0:
        #         good += r-l
        #     while len(nums_dict) > k:
        #         nums_dict[nums[l]] -= 1
        #         l += 1
        #         if nums_dict[l] == 0:
        #             del nums_dict[r]
        #             if r-l == k:
        #                 good += r-l
        #             break
        # return good
                
        # for r in range(len(nums)):
        #     nums_dict[nums[r]] += 1

        #     while len(nums_dict) > k:
        #         good += (r-l)
        #         if nums_dict[l] == 0:
        #             del nums_dict[r]
        #         l += 1
