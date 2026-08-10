class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        left, right = 0, 0
        curr = 0
        while right < len(nums):
            curr += nums[right]
            right += 1
            while curr >= target:
                min_size = min(min_size, right - left)
                curr -= nums[left]
                left += 1
        return min_size if min_size != float("inf") else 0

        