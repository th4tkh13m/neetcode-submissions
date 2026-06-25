class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We do sliding window, but the left pointer keeping on the smallest
        
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit