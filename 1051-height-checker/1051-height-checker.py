class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        
        mismatches = 0

        for i in range(len(heights)):
            if(heights[i] != expected[i]):
                mismatches += 1

        return mismatches