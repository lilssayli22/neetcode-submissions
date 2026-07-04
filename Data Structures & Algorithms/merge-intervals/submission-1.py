class Solution:
    def merge(self, intervals):
        def sort_by_start(intervals):
            return sorted(intervals, key=lambda x: x[0])
        def overlap(x1, x2):
            return x1[1] >= x2[0] and x2[1] >= x1[0]
        intervals = sort_by_start(intervals)
        l = [intervals[0]]
        i = 1
        while i < len(intervals):
            if overlap(l[-1], intervals[i]):
                l[-1]  = [l[-1][0],max (l[-1][1],intervals[i][1])]
            else : 
                l.append(intervals[i])
            i+=1 
        return l  