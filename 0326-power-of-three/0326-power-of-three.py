class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False

        power = 1

        while(power < n):
            power *= 3

        if(power == n):
            return True
        else:
            return False