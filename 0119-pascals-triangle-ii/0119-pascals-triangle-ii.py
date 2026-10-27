class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        ans = [1]
        res = 1
        for i in range(1, n+1):
            res = res * (n - i + 1)
            res = res // i
            ans.append(res)
        
        return ans