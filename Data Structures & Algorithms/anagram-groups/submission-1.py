class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        res = []

        for i, word in enumerate(strs):
            character_count = [0] * 26
            for c in word:
                character_count[ord(c) - 97] += 1
            character_count_tuple = tuple(character_count)
            if (character_count_tuple in dict_strs):
                dict_strs[character_count_tuple].append(i)
            else:
                dict_strs[character_count_tuple] = [i]    

        for indices in dict_strs.values():
            res.append([strs[i] for i in indices])
        
        return res
