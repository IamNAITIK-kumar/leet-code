class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 1
        suffix = 1
        ans = float('-inf')  #represents the minimum value
        n = len(nums)
        for i in range(n):
            if(prefix == 0):
                prefix = 1
            if(suffix == 0):
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]
            ans = max(ans , max(prefix, suffix))
    
        return ans