class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        XOR = 0
        for i in range(len(nums)):
            XOR = XOR ^ nums[i]

        return XOR
        