class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            c = s[right]
            right += 1
            count[c] += 1
            while (right - left) - max(count.values()) > k:
                d = s[left]
                left += 1
                count[d] -= 1
            longest = max(longest, right - left)
        return longest
        