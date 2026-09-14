class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0
        right = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            window[c] += 1
            k = len(s1)
            while right - left > k:
                d = s2[left]
                left += 1
                window[d] -= 1
            if right - left == k and need == window:
                return True
        return False