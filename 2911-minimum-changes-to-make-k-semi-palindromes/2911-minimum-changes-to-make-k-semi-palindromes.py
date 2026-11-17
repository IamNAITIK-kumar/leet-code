
class Solution(object):
    def minimumChanges(self, s, k):

        n = len(s)

        # Step 1: Precompute cost of every substring
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                length = j - i + 1
                mini = float('inf')

                # Try every valid divisor
                for d in range(1, length):

                    if length % d == 0:

                        cnt = 0

                        # Compare characters in each group
                        for offset in range(d):

                            left = i + offset
                            right = j - d + 1 + offset

                            while left < right:

                                if s[left] != s[right]:
                                    cnt += 1

                                left += d
                                right -= d

                        mini = min(mini, cnt)

                cost[i][j] = mini

        # Step 2: DP
        dp = [[float('inf')] * (k + 1)
              for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):

            for parts in range(1, k + 1):

                for end in range(i + 1, n):

                    dp[i][parts] = min(
                        dp[i][parts],
                        cost[i][end] + dp[end + 1][parts - 1]
                    )

        return dp[0][k]
