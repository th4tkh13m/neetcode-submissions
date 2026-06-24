class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        
        for string in strs:
            # Build the key for the hashmap
            string_map = [0] * 26
            for c in string:
                string_map[ord(c) - ord("a")] += 1
            
            key = tuple(string_map)

            if not key in ana_map:
                ana_map[key] = [string]
            else:
                ana_map[key].append(string)
        
        return list(ana_map.values())
