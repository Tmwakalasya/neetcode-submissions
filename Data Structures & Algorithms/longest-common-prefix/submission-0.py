class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        current_lcp = strs[0]
        for i in range(1, len(strs)):
            current_string = strs[i]

            k = 0
            while k < len(current_lcp) and k < len(current_string) and current_string[k] == current_lcp[k]:
                k += 1
            current_lcp = current_lcp[0:k]
        return current_lcp

        if not current_lcp:
            return ""

        