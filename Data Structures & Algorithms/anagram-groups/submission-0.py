class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def findAnagrams(str1: str, str2: str):
            count1 = {}
            count2 = {}

            for c in str1:
                if not c in count1:
                    count1[c] = 1
                else:
                    count1[c] += 1
            
            for c in str2:
                if not c in count2:
                    count2[c] = 1
                else:
                    count2[c] += 1
            return count1 == count2

        group_map = {strs[0]: [strs[0]]}
        keys = [strs[0]]
        for string in strs[1:]:
            found = False

            for k in keys:

                if findAnagrams(k, string):
                    found = True
                    group_map[k].append(string)
            if not found:
                keys.append(string)
                group_map[string] = [string]
        res = []
        for val in group_map.values():
            res.append(val)
        return res

        