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

        pos_speed_map = {position[i]: speed[i] for i in range(len(position))}

        sorted_position = sorted(position)
        stack = []
        for i in range(len(position)):
            if not stack:
                stack.append(i)
                continue
            
            while len(stack) > 0 and ((target - sorted_position[i]) / pos_speed_map[sorted_position[i]]) >= ((target - sorted_position[stack[-1]]) / pos_speed_map[sorted_position[stack[-1]]]):
                stack.pop()
            stack.append(i)

        return len(stack)
