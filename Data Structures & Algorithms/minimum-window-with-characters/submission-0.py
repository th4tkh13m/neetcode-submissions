class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checkValidSubstring(count_map):
            for k, v in count_map.items():
                if v > 0:
                    return False
            return True

        n = len(s)
        m = len(t)

        if m == 1:
            if not t in s:
                return ""
            else:
                return t
        
        if n == 1:
            return ""

        count_map = {}
        for c in t:
            count_map[c] = count_map.get(c, 0) + 1
        
        # sliding window
        left = 0
        right = 0

        min_substring = ""

        while right < n:
            if not s[right] in count_map:
                right += 1

                
            else:
                count_map[s[right]] -= 1

                while checkValidSubstring(count_map):
                    if left < right:
                        if min_substring == "" or len(min_substring) > (right - left + 1):
                            min_substring = s[left: right+1]
                        if s[left] in count_map:
                            count_map[s[left]] += 1
                        left += 1
                right += 1
        return min_substring