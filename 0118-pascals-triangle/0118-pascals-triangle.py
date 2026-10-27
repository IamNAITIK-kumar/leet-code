class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for n in range(numRows):
            row = [1]
            res = 1

            for i in range(1, n + 1):
                res = res * (n - i + 1) // i
                row.append(res)
            
            ans.append(row)

        return ans