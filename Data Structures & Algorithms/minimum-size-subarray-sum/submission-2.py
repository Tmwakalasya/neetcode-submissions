class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        min_size = float('inf')
        left, right = 0, 0
        while right < len(nums):
            c = nums[right]
            right += 1
            curr += c
            while curr >= target:
                min_size = min(min_size, right - left)
                d = nums[left]
                left += 1
                curr -= d
        return min_size if min_size != float('inf') else 0
        