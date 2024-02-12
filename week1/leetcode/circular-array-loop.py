class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                continue
                
            slow = i
            fast = i
            
            while nums[slow] * nums[(fast := (fast + nums[fast]) % n)] > 0 and nums[slow] * nums[(fast := (fast + nums[fast]) % n)] > 0:
                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break  
                    return True
                slow = (slow + nums[slow]) % n
                
        return False
