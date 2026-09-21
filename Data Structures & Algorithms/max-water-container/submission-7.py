class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = (r - l)
            height = min(heights[l], heights[r])
            curr = width * height
            if curr > maxarea:
                maxarea = curr
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxarea
        