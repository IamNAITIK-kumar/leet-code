class Solution(object):

    def BS(self, nums, low, high, target):
        if(low > high):
            return -1
        mid = (high + low)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid] < target):
            return self.BS(nums, mid+1, high, target)

        return self.BS(nums,low, mid-1, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.BS(nums, 0, (len(nums)-1), target)
        