class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            cost = prices[i] - mini
            maxprofit = max(maxprofit, cost)
            mini = min(mini, prices[i])

        return maxprofit