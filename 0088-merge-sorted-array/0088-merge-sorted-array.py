class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = 0
        
        while(left >= 0 and right < n):
            if(nums1[left] >= nums2[right]):
                nums1[left], nums2[right] = nums2[right],nums1[left]
                left -= 1
                right += 1

            else:
                break
        
        nums1[:m] = sorted(nums1[:m])
        nums2.sort()

        for i in range(n):
            nums1[m + i] = nums2[i]

        
        