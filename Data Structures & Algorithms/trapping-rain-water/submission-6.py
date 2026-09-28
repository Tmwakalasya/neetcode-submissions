class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        tallest = 0
        for i in range(n):
            tallest = max(tallest, height[i])
            left_max[i] = tallest
        tallest = 0
        for j in range(n - 1, -1, -1):
            tallest = max(tallest, height[j])
            right_max[j] = tallest
        total = 0
        for i in range(n):
            total += min(right_max[i], left_max[i]) - height[i]
        return total
        