class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt1 = 0
        cnt2 = 0
        ele1 = 0
        ele2 = 0

        for i in range(len(nums)):
            if(cnt1 == 0 and ele2 != nums[i]):
                cnt1 = 1
                ele1 = nums[i]
            elif(cnt2 == 0 and ele1 != nums[i]):
                cnt2 = 1
                ele2 = nums[i]
            elif(nums[i] == ele1):
                cnt1 += 1
            elif(nums[i] == ele2):
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(nums)):
            if(ele1 == nums[i]):
                cnt1 += 1
            if(ele2 == nums[i]):
                cnt2 += 1
        
        mini = (len(nums) // 3) + 1

        ls = []

        if(cnt1 >= mini):
            ls.append(ele1)
        if(cnt2 >= mini and ele2 != ele1):
            ls.append(ele2)
        
        ls.sort()

        return ls