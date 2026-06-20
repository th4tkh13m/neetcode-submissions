class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = [0] * 26
        for c in s:
            char_map[ord(c) - ord("a")] += 1
        for c in t:
            char_map[ord(c) - ord("a")] -= 1
        
        for c in char_map:
            if c != 0:
                return False
        return True