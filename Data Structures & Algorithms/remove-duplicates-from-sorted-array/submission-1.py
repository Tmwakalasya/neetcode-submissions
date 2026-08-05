class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[slow] = nums[right]
                slow += 1
        return slow

        