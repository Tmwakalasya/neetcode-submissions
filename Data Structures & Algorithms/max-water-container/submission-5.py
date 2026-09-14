class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = (r - l)
            height = min(heights[l], heights[r])
            curr_area = width * height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = max(area, curr_area)
            
        return area
        