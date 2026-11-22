class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for string in strs:
            char_count = [0] * 26
            for c in string:
                char_count[ord(c) - ord("a")] += 1
            
            key = tuple(char_count)
            anagram_map[key] = anagram_map.get(key, []) + [string]
        
        return list(anagram_map.values())