class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_idx = {}  
        for i, interval in enumerate(intervals):
            start_idx[interval[0]] = i
        
        sorted_starts = sorted(start_idx.keys())
        
        ans = []
        for interval in intervals:
            end = interval[1]
            left = 0
            right = len(sorted_starts) - 1
            idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_starts[mid] >= end:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            if idx == -1 or idx == len(sorted_starts):
                ans.append(-1)
            else:
                start = sorted_starts[idx]
                ans.append(start_idx[start]) 
            
        return ans