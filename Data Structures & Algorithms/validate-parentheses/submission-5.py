class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "}":"{","]":"["}
        for c in s:
            if c in par:
                if not stack or stack[-1] != par[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
        