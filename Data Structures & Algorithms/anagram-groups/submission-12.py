class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 1:
            return [strs]
        
        anagram_dict = {}

        for string in strs:
            char_map = [0] * 26
            for c in string:
                char_map[ord(c) - ord("a")] += 1
            
            tuple_map = tuple(char_map)

            anagram_dict[tuple_map] = anagram_dict.get(tuple_map, []) + [string]
        

        return list(anagram_dict.values())