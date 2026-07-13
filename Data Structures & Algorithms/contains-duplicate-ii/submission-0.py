class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        left = 0
        for right in range(len(nums)):
            while right - left > k:
                window_set.remove(nums[left])
                left += 1
            if nums[right] in window_set:
                return True
            window_set.add(nums[right])
        return False
        