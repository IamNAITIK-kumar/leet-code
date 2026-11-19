class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if(n <= 3):
            return 0
        
        nums.sort()

        ans = min(
            nums[n-1] - nums[2],
            nums[n-2] - nums[1],
            nums[n-3] - nums[0]
        )

        return ans