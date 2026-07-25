class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack to keep track of the temperature where we pop elements
        # in the stack when the added value is greater than the top value.
        # This allows us to add to the result array the diff of indices
        stack = [] # (Temp, Index)
        res = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            # Check if current temp > temp on stack
            while stack and val > stack[-1][0]:
                add_val, add_idx = stack.pop()
                res[add_idx] = idx - add_idx
            
            stack.append([val, idx])
        
        return res
