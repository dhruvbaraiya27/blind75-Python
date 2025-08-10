"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        
        last_end = intervals[0].end
        for meeting in intervals[1:]:
            if meeting.start < last_end:
                return False
            else:
                last_end = meeting.end
        return True
