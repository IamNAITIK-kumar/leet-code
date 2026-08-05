class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * max(2, n + 1)
        f[0] = 0
        f[1] = 1

        if n == 0:
            return (f[0])
        elif n == 1:
            return (f[1])
        else:
            for i in range(2, n + 1):
                f[i] = f[i - 1] + f[i - 2]
            return (f[n])