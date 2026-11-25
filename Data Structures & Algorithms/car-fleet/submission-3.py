class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Idea: Check from the car have highest position -> lowest position
        # Check if that lower car can catch the car in front?
        # How to check?
        # If spe 1 = spe 2 => False never catch
        # pos 1 + spe 1 * t = pos 2 + spe 2 * t => pos 2 - pos 1 = (spe 1 - spe 2) * t => (pos 2 - pos 1) / (spe1-spe2) = t
        # meet = pos 1 + spe1 *  (pos 2 - pos 1) / (spe1-spe2) 
        # If meet > target or meet <= 0 => False

        # :Use stack from highest pos to lowest pos
        #???

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []


        for p, s in pair:
            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
