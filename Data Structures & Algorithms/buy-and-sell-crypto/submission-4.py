class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = float('-inf')
        curr_pr = 0
        min_pr = float('inf')
        for p in prices:
            if p < min_pr:
                min_pr = p
            curr_pr = p - min_pr
            max_prof = max(max_prof, curr_pr)
        return max_prof 


        