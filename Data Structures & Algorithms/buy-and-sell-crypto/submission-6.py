class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for p in prices:
            if p < min_price:
                min_price = p
            curr_profit = p - min_price
            max_profit = max(max_profit, curr_profit)
        return max_profit
            