class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = [0] * 26
            # count the c in s + 1
            # count the c in t - 1
            # if all ele not == 0 => False
            # else True
        for c in s:
            count_map[ord(c) - ord("a")] += 1
        for c in t:
            count_map[ord(c) - ord("a")] -= 1
        
        for c in count_map:
            if c != 0:
                return False
        return True