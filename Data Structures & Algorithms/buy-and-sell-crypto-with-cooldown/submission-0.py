class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Cache result from current index
        dp = {} # {(i, buying curr idx), max profit}

        def dfs(i, buying):
            # Base Cases:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # If buying, you can't buy more than 1
                buy = dfs(i + 1, False) - prices[i]
                # If on cooldown, you can still buy
                cooldown = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # If selling, you can't use the next one, but you can buy
                sell = dfs(i + 2, True) + prices[i]
                # Otherwise, you are holding a NeetCoin and you are looking for selling price
                cooldown = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
            

