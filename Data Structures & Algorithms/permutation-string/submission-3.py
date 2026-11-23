class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a char count for each substring and slide
        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord("a")] += 1
        
        count_substring_s2 = [0] * 26
        for c in s2[:len(s1)]:
            count_substring_s2[ord(c) - ord("a")] += 1
        
        for left in range(len(s2) - len(s1) + 1):
            print(count_s1)
            print(count_substring_s2)
            if count_s1 == count_substring_s2:
                return True

            
            count_substring_s2[ord(s2[left]) - ord("a")] -= 1
            if left + len(s1) < len(s2):
                count_substring_s2[ord(s2[left + len(s1)]) - ord("a")] += 1
        return False 