class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = prices
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                Fi= stack.pop()
                ans[Fi] = prices[Fi] - prices[i]
            stack.append(i)
        return ans