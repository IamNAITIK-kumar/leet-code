class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()                                   

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            x = 0

            for i in str(n):
                x = int(i) ** 2 + x

            n = x

        return True