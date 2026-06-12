class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for string in strs:
            len_str = len(string)
            res_str += (f"{len_str}#" + string)
        return res_str
    def decode(self, s: str) -> List[str]:
        length = 0
        strs = []
        i = 0
        while i < len(s):
            
            j = i + 1
            while j < len(s):
                if s[j] == "#":
                    length = int(s[i:j])
                    break
                else: j+=1
            i = j + 1
            strs.append(s[i: i + length])
            i += (length)
        return strs



