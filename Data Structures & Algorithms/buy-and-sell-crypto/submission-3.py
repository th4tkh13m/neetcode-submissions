class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Idea: store the maximum price
        # keep the left side of the window at the one that has max price (expected to be min)
        # Continue sliding the right side
        # If there is better price, update
        min_day = 0
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[min_day]
            max_profit = max(max_profit, profit)

            if prices[min_day] > prices[i]:
                min_day = i
        return max_profit