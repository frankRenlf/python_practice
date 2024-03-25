from typing import List


class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] += dp[i - c] + 1
        print(dp)
        return dp[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        print(dp)
        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    sol.change(amount=5, coins=[1, 2, 5])
