class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            prefixsum = 0

            for j in range(i, min(i+r, n)):
                prefixsum += nums[j]

                length = j - i + 1

                if(length >= l and prefixsum > 0):
                    ans = min(ans, prefixsum)
                
        return -1 if ans == float('inf') else ans    