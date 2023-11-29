class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rt=0
        ch =x
        if x<0:
            return False
        while x>9:
            rt = (rt*10) + x%10
            x= (x-x%10)/10
        rt = (rt*10) + x
        if rt==ch:
            return True
        else:
            return False