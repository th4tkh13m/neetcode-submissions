class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if (c == ")" and stack.pop() != "(") or (c == "]" and stack.pop() != "[") or (c == "}" and stack.pop() != "{"):
                    return False
        return len(stack) == 0
                