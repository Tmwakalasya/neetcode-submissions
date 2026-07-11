class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() 
        duplicates = set()
        for n in nums:
            if n in seen:
                duplicates.add(n)
                return True
            seen.add(n)
        return False
         