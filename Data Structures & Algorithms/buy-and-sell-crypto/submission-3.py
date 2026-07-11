class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        curProfit = 0
        # Loop through the prices
        for p in prices:
            if p < minPrice:
                minPrice = p
            curProfit = p - minPrice
            maxProfit = max(maxProfit, curProfit)
        return maxProfit
            
        