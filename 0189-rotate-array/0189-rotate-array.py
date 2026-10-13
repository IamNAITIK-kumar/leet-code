class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 

        k = k % len(nums)

        if k > 0 :
        
            nums[-k : ] = reversed(nums[-k : ])
            nums[0 : (len(nums) - k)] = reversed(nums[0 : (len(nums) - k)])
            nums.reverse()

        return nums
