class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_map = defaultdict(int)
        longest = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            char_map[c] += 1
            while char_map[c] > 1:
                d = s[left]
                left += 1
                char_map[d] -= 1
            longest = max(longest, right - left)
        return longest


        