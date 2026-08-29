class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (Temp, Index)
        res = [0] * len(temperatures)

        # Essentially, we are looking and poping off the stack if the current day is warmer (most recent highest temp on top)
        # Update the previous index that was a high with the difference in the current index from the previous as we now have a higher temp
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                add_val, add_idx = stack.pop()
                res[add_idx] = idx - add_idx
            
            stack.append([val, idx])
        
        return res