class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = (r - l)
            height = min(heights[l], heights[r])
            curr = width * height
            if curr > max_area:
                max_area = curr
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, curr)
        return max_area
        