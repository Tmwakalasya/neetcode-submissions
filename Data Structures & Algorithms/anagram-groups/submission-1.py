class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            sorted_wrd = "".join(sorted(word))
            map[sorted_wrd].append(word)
        return list(map.values())

        