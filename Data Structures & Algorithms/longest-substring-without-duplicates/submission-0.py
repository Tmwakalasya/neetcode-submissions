class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep a set of letters
        char_set = set()
        left = 0
        best = 0

        for right in range(len(s)):
            # The character that could break the window is the incoming one
            # Meaning that we have already seen it in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            best = max(best, right - left + 1)
        return best
        