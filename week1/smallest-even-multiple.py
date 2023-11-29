class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return n 
        num = n*2
        for i in range(num):
            if num%2 == 0 and num%n==0:
                return num