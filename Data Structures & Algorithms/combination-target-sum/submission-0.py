class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(index,path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            if curSum > target:
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num + curSum <= target:
                    path.append(candidates[i])
                    backtracking(i,path,curSum + candidates[i])
                    path.pop()
        backtracking(0, [], 0)
        return res

        