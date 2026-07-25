class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Store the min_price and check if the current profit 
        # is better than the max_profit
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)

            min_price = min(min_price, price)
            
        return max_profit