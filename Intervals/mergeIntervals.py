class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key = lambda x: x[0])
        i=0
        res = []
        n = len(intervals)
        for s,e in intervals:
            if not res or s > res[-1][1]:
                res.append([s,e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
            

