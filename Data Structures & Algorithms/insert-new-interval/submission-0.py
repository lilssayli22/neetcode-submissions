class Solution:
    def insert(self, intervals, newInterval):
        def overlap(x1,x2): 
            if (x1[1]<x2[0] or x2[1]<x1[0]) :
                return False
            else:
                return True
        l = []
        i=0
        if not intervals:
            l.append(newInterval)
            return l
        while i < len(intervals) and newInterval !=None:
            if intervals[i][0]<newInterval[0] : 
                if not overlap(intervals[i], newInterval) :
                    l.append(intervals[i])
                else : 
                    l.append([intervals[i][0],max(intervals[i][1],newInterval[1])])
                    newInterval = None
                i+=1
            else :
                 l.append(newInterval)
                 newInterval = None
        if i == len(intervals) and newInterval != None:
            l.append(newInterval)
            return l
                 
        for j in range(i,len(intervals)):
            if overlap(intervals[j], l[-1]):
                l[-1] = [l[-1][0] , max(l[-1][1],intervals[j][1]) ]
            else : 
                l.append(intervals[j])
        return l