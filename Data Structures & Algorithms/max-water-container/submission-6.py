class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l <= r:
            width = (r - l)
            height = min(heights[l], heights[r])
            curr_area = width * height
            if curr_area > area:
                area = curr_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = max(area, curr_area)
        return area

        