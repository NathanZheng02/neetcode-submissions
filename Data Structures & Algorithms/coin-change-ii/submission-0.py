class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(1, len(dp)):
                if coin <= a:
                    dp[a] += dp[a - coin]

            print("Coin ", coin, " and Updated dp: ", dp)
        return dp[-1]

        # Memoization
        # cache = {} # (Total, Valid)

        # def dfs(i, a):
        #     if a == 0:
        #         return 1
        #     if i >= len(coins):
        #         return 0
        #     if cache[]
        
        # return dfs(0, amount)

