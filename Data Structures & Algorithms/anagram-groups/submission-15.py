class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        anagram_map = defaultdict(list)

        for string in strs:
            char_count = [0] * 26

            for c in string:
                char_count[ord(c) - ord("a")] += 1
            
            key = tuple(char_count)
            anagram_map[key].append(string)
        
        return list(anagram_map.values())
        