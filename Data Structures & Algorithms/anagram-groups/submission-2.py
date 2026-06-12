class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in group_map:
                group_map[key].append(string)
            else:
                group_map[key] = [string]
        return list(group_map.values())

        