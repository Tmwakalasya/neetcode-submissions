class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}":"{", "]":"[", ")":"("}
        stk = []
        for c in s:
            if c in map:
                if not stk or stk[-1] != map[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return len(stk) == 0
        