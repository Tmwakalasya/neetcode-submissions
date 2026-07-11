class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We want to build a list of anagrams based on a key
        # They key could be the sorted word and the list of anagrams be
        # The different variations of words we could form from the key
        map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            map[key].append(word)
        return list(map.values())
        