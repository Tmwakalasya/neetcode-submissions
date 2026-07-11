class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
        for j in t:
            if j in count_t:
                count_t[j] += 1
            else:
                count_t[j] = 1
        return count_s == count_t 
        