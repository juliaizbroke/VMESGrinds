class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        half_k = k // 2
        
        original_profit = sum(strategy[i] * prices[i] for i in range(n))
        
        current_delta = 0

        for i in range(half_k):
            current_delta += (0 - strategy[i]) * prices[i]

        for i in range(half_k, k):
            current_delta += (1 - strategy[i]) * prices[i]
        
        max_delta = max(0, current_delta)
        
        for start in range(1, n - k + 1):
            left_out = start - 1
            current_delta -= (0 - strategy[left_out]) * prices[left_out]
            
            right_in = start + k - 1
            current_delta += (1 - strategy[right_in]) * prices[right_in]
            
            middle = start + half_k - 1

            current_delta -= (1 - strategy[middle]) * prices[middle]

            current_delta += (0 - strategy[middle]) * prices[middle]
            
            max_delta = max(max_delta, current_delta)
        
        return original_profit + max_delta