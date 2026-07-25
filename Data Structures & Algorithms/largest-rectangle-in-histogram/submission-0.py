class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack with (idx, height)
        # If greater, then we just add
        # If not greater, then we gotta pop and record max area.
        # Repeat pop until the top value "can be extended" (leq
        # current height). The current element "steals" the index
        # of the ones it popped.
        # At the end, compute area of remaining ones

        stack = [] # (Index, Height)
        max_area = 0

        for i, h in enumerate(heights):
            # Start idx just in case you can extend backwards
            start = i

            # Check if curr height is greater than the one on the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            
            stack.append((start, h))

        # Now check for remaining entries
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area
