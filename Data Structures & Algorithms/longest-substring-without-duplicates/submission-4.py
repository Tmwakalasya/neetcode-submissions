class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        longest = 0
        left = 0
        right = 0
        while right < len(s):
            c = s[right]
            right += 1
            counter[c] += 1
            while counter[c] > 1:
                d = s[left]
                left += 1
                counter[d] -= 1
            longest = max(longest, right - left)
        return longest 
        