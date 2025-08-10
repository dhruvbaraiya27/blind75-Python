"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        for iv in intervals[1:]:
            if iv.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, iv.end)
        
        return len(min_heap)
        
