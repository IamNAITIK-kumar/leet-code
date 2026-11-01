class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mpp = {}
        ans = []

        for i in nums1:
            mpp[i] = mpp.get(i, 0) + 1

        for i in nums2:
            if i in mpp and mpp[i] > 0:
                ans.append(i)
                mpp[i] -= 1

        return ans
        