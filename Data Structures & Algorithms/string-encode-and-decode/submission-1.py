class Solution:

    def encode(self, strs: List[str]) -> str:
        tokenized = []
        for string in strs:
            tokenized.append("<bos>" + string + "<eos>")
        return "<special>".join(tokenized)
    def decode(self, s: str) -> List[str]:
        tokenized = s.split("<special>")
        strs = []
        for string in tokenized:
            if "<bos>" in string and "<eos>" in string:
                strs.append(string[5:-5])
        return strs
