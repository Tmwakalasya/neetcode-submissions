class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        best = float('inf')
        cur = 0
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= target:
                best = min(best, right - left + 1)
                cur -= nums[left]
                left += 1
        return 0 if best == float('inf') else best


        