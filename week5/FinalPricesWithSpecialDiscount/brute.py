class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        if n <= 1:
            return prices
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices