"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted([[interval.start, interval.end] for interval in intervals])
        i = 0
        n = len(intervals)

        while i < n - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                return False
            i += 1
        return True