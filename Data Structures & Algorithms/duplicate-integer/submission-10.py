class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen, duplicate = set(), set()
        for num in nums:
            if num in seen:
                duplicate.add(num)
                return True
            seen.add(num)
        return False
        