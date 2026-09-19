class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for c in t:
            if chars.get(c) == 1:
                chars.pop(c)
            else:
                chars[c] = chars.get(c, 0) - 1
        return not chars