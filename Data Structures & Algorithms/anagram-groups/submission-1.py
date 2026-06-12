class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in group_map:
                group_map[sorted_string].append(string)
            else:
                group_map[sorted_string] = [string]
        return list(group_map.values())

        