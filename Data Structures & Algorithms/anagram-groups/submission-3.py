class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - 97] += 1
            sublists[tuple(chars)].append(word)

        return list(sublists.values())
