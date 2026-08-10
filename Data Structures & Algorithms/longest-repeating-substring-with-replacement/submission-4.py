class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = defaultdict(int)
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            freq[c] += 1
            while (right - left) - max(freq.values()) > k:
                d = s[left]
                left += 1
                freq[d] -= 1
            longest = max(longest, right - left)
        return longest

        