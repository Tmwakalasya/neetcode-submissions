class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## tea, ate, if you sort this it becomes aet, aet
        map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            map[sorted_word].append(word)
        return list(map.values())
        