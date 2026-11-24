class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        left = 0
        right = 0
        profit = 0

        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit
