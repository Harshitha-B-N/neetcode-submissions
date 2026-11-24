class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_dict = {}
        for i in strs:
            word = "".join(sorted(i))
            grp_dict[word] = grp_dict.get(word, []) + [i]

        return list(grp_dict.values()) 
        