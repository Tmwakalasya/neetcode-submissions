class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            c = s[right]
            right += 1
            map[c] += 1
            while map[c] > 1:
                d = s[left]
                left += 1
                map[d] -= 1
            longest = max(longest, right - left)
        return longest