class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = [0] * 26
        char_count_t = [0] * 26

        for c in s:
            char_count_s[ord(c) - ord("a")] += 1
        
        for c in t:
            char_count_t[ord(c) - ord("a")] += 1
        
        return char_count_s == char_count_t
        