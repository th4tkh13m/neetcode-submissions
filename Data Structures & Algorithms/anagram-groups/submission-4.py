class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap the map all anagrams under same key

        anagram_map = {}

        for string in strs:
            # If we dont have the anagram key, we create it
            count_list = [0] * 26
            for c in string:
                count_list[ord(c) - ord("a")] += 1
            key = tuple(count_list)

            if not key in anagram_map:
                anagram_map[key] = [string]
            else:
                anagram_map[key].append(string)
            
        return list(anagram_map.values())