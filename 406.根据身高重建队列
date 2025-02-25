# 贪心算法
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        ans = []
        for p in people:
            if p[1]>=len(ans):
                ans.append(p)
            elif p[1]<len(ans):
                ans.insert(p[1],p)
        return ans
