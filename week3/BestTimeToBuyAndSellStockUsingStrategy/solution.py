class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        
        def calculate_profit(strat):
            total = 0
            for i in range(len(strat)):
                total += strat[i] * prices[i]
            return total
        
        original_profit = calculate_profit(strategy)
        max_profit = original_profit
        
        for start in range(n - k + 1):
            modified_strategy = strategy.copy()
            
            half_k = k // 2
            
            for i in range(start, start + half_k):
                modified_strategy[i] = 0
            
            for i in range(start + half_k, start + k):
                modified_strategy[i] = 1
            
            new_profit = calculate_profit(modified_strategy)
            
            max_profit = max(max_profit, new_profit)

        return max_profit
        