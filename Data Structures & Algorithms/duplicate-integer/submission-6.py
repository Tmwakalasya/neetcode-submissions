class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen, duplicates = set(), set()
        for num in nums:
            if num in seen:
                duplicates.add(num)
                return True
            seen.add(num)
        return False
         