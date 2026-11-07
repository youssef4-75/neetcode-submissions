class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = end = 0
        max_profit = 0
        for i, p in enumerate(prices):
            if p<prices[start]:
                start = i
            if p - prices[start] > max_profit:
                max_profit = p - prices[start]
        return max_profit
            
        