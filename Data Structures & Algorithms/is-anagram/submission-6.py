class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map_s = [0] * 26
        char_map_t = [0] * 26

        for c in s:
            char_map_s[ord(c) - ord("a")] += 1
        
        for c in t:
            char_map_t[ord(c) - ord("a")] += 1
        
        return char_map_s == char_map_t