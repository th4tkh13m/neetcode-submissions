class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 0:
            return 0
        idx_stack = []
        result = [0] * n
        for i in range(n):
            if not idx_stack:
                idx_stack.append(i)
                continue
            while len(idx_stack) > 0 and temperatures[i] > temperatures[idx_stack[-1]]:
                idx = idx_stack.pop()
                result[idx] = i - idx
            
            idx_stack.append(i)
        
        return result
            