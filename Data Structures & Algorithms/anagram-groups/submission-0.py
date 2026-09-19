class Solution:
    def createHistogram(self, str1: str) -> frozenset:
        chars = {}
        for c in str1:
            chars[c] = chars.get(c, 0) + 1
        return frozenset(chars.items())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            histogram = self.createHistogram(word)
            if histogram not in anagrams.keys():
                anagrams[histogram] = [word]
            else:
                anagrams[histogram].append(word)
        result = list(anagrams.values())
        return result
    