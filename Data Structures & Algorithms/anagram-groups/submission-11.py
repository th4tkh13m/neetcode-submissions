class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Idea: count by hashmap
        # Then having the hashmap into tuple so that immutable
        # => group into dict
        def get_key(string):
            count_dict = {}
            for c in string:
                count_dict[c] = count_dict.get(c, 0) + 1
            count_set = set()
            for k, v in count_dict.items():
                count_set.add((k, v))
            return tuple(sorted(count_set))
        anagram_dict = {}

        for string in strs:
            key = get_key(string)
            # print(key)
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]
        return list(anagram_dict.values())        