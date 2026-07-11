class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # Key is the number, value is its index
        for i, j in enumerate(nums):
            diff = target - j
            if diff in seen:
                return [seen[diff], i]
            seen[j] = i

        