class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        for i in range(len(t)):
            countS[t[i]] = countS.get(t[i], 1) - 1
        
        for value in countS.values():
            if value != 0:
                return False
        return True