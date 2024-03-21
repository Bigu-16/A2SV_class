class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sorted_arr(left_half, right_half):
            left = 0
            right = 0
            ans = []
            while left < len(left_half) or right < len(right_half):
                if  ((left < len(left_half) and right < len(right_half)) and left_half[left] <= right_half[right]) or (left <                   len(left_half) and right == len(right_half)):
                    ans.append(left_half[left])
                    left += 1
                else:
                    ans.append(right_half[right])
                    right += 1
            
            return ans

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return sorted_arr(left_half, right_half)
        
        return mergeSort(0,len(nums) - 1,nums)