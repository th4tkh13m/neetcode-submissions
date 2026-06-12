class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_1 = {}
        count_2 = {}
        for c in s:
            if not c in count_1:
                count_1[c] = 1
            else:
                count_1[c] += 1
        for c in t:
            if not c in count_1:
                return False
            if not c in count_2:
                count_2[c] = 1
            else:
                count_2[c] += 1
        
        return count_1 == count_2

        