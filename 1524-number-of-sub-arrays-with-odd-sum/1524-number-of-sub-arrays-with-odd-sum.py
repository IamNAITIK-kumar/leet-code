class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odd = 0
        even = 1
        cnt = 0
        prefix_sum = 0
        MOD = 10 ** 9 + 7

        for num in arr:
            prefix_sum += num

            if((prefix_sum % 2) == 0):
                cnt += odd
                even += 1
            else:
                cnt += even
                odd += 1

        return cnt % MOD