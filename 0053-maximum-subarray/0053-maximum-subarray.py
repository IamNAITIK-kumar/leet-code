class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        maxi = float("-inf")

        for i in range(len(nums)):
            sum += nums[i]

            if(sum >  maxi):
                maxi = sum

            if(sum < 0):
                sum = 0

        return maxi