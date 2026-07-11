class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        L = 0
        R = len(height) - 1
        curr_area = 1
        while L < R:
            width = R - L
            curr_height = min(height[L],height[R])
            curr_area = width * curr_height
            if curr_area > max_area:
                max_area = curr_area
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_area

        