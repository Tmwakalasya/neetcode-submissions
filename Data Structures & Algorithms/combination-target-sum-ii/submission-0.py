class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(index, path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target:
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if num + curSum <= target:
                    path.append(candidates[i])
                    backtracking(i + 1, path, candidates[i] + curSum)
                    path.pop()
        backtracking(0, [], 0)
        return res
        