class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        longest = 0
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            right += 1
            count[c] += 1
            while count[c] > 1:
                d = s[left]
                left += 1
                count[d] -= 1
            longest = max(longest, right - left)
        return longest
        