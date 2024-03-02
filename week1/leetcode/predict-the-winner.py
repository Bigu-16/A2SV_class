class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score(left,right):
            if  left == right:
                return nums[left]
            
            ch1 = nums[left] - score(left+1, right)
            ch2 = nums[right] - score(left, right-1)

            return (max(ch1,ch2))

        return True if score(0,(len(nums)-1)) >= 0 else False
