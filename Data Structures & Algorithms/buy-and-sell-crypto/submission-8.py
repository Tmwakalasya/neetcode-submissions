class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float("inf")
        for p in prices:
            if p < min_price:
                min_price = p
            curr_prof = p - min_price
            max_prof = max(max_prof, curr_prof)
        return max_prof
        