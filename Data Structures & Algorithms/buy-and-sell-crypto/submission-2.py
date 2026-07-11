class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxProfit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            curr_profit = price - lowest
            maxProfit = max(maxProfit, curr_profit)
        return maxProfit
        