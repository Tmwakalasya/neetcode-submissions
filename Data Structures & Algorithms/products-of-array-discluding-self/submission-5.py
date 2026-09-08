class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pfx = [1] * n
        sfx = [1] * n
        ans = [1] * n
        # pfx
        for i in range(1, n):
            pfx[i] = pfx[i - 1] * nums[i - 1]
        # sfx
        for i in range(n - 2, -1, -1):
            sfx[i] = sfx[i + 1] * nums[i + 1]
        # ans

        for i in range(n):
            ans[i] = pfx[i] * sfx[i]
        return ans

        