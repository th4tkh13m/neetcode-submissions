class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def findCount(s: str):
            char_map = [0] * 26
            for c in s:
                char_map[ord(c) - ord("a")] += 1
            return tuple(char_map)
        group_map = {}
        for string in strs:
            char_map = findCount(string)
            if not char_map in group_map:
                group_map[char_map] = [string]
            else:
                group_map[char_map].append(string)
        return list(group_map.values())