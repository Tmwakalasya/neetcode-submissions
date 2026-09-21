class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_max = [0] * n
        left_max = [0] * n
        longest = 0
        for i in range(n):
            longest = max(longest, height[i])
            left_max[i] = longest
        longest = 0
        for i in range(n - 1, -1, -1):
            longest = max(longest, height[i])
            right_max[i] = longest
        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]
        return total

        