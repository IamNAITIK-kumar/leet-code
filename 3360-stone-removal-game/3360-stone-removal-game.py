class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        take = 10
        steps = 0

        while(take <= n):
            n -= take
            take -= 1
            steps += 1
        
        if((steps % 2) == 1):
            return True
        else:
            return False