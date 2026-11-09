class Solution(object):
    def findMismatchedSegments(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[List[str]]
        """
        a = []
        i = 0
        while(i < len(s1)):
            if(s1[i] == s2[i]):
                i += 1
            else:
                j = i
                while(i < len(s1) and s1[i] != s2[i]):
                    i += 1
                a.append([s1[j:i], s2[j:i]])
            
        return a