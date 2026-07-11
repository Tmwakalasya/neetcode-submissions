class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(index, path):
            if index == len(nums):
                res.append(path[:])
                return
            # Take nums[index]
            path.append(nums[index])
            backtracking(index + 1, path)
            # Pop back to the previous branch
            path.pop()

            # Explore other branches
            backtracking(index + 1, path)
        backtracking(0, [])
        return res

        