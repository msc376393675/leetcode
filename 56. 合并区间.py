class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        ans = []
        l = intervals[0][0]
        r = intervals[0][1]
        for i in range(1,len(intervals)):
            if r >= intervals[i][0]:
                r = max(r,intervals[i][1])
            else:
                ans.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        ans.append([l,r])
        return ans   
