"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([j.end for j in intervals])

        maxi, ongoing = 0, 0
        start, end = 0, 0
        while start < len(intervals):
            if startTimes[start] < endTimes[end]:
                start += 1
                ongoing += 1
            else:
                end += 1
                ongoing -= 1
            maxi = max(maxi, ongoing)
        return maxi

        