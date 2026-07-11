class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = set()
        for n in nums:
            if n in seen:
                return True
                duplicates.add(n)
            else:
                seen.add(n)
        return False


         