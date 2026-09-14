class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = defaultdict(int)
        longest = 0
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            right += 1
            map[c] += 1
            while (right - left) - max(map.values()) > k:
                d = s[left]
                left += 1
                map[d] -= 1
            longest = max(longest, right - left)
        return longest

