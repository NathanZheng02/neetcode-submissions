class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting by start times, similar to previous question
        intervals.sort(key = lambda pair : pair[0])
        res = [intervals[0]]

        for start, end in intervals:
            prevStart, prevEnd = res[-1]

            if start <= prevEnd:
                # Merge
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
        return res