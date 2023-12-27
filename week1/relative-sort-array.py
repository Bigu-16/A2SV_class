class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_dict = {}
        count = [0]*len(arr2)
        ans = [0]*len(arr1)
        extra = []

        for i,value in enumerate(arr2):
            arr_dict[value] = i

        for num in arr1:
            if num in arr_dict:
                count[arr_dict[num]] += 1
            else:
                extra.append(num)

        ptr = 0
        for i in range(len(arr2)):
            for _ in range(count[i]):
                ans[ptr] = arr2[i]
                ptr += 1

        extra.sort()
        for num in extra:
            ans[ptr] = num
            ptr += 1

        return ans
