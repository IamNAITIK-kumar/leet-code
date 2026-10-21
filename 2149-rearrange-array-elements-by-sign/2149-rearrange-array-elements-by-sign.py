class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negative = 1
        positive = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if(nums[i] < 0):
                ans[negative] = nums[i]
                negative += 2
            else:
                ans[positive] = nums[i]
                positive += 2
        
        return ans