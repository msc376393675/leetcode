class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for x in s:
            counts[x] = counts.get(x,0)+1
        sorted_count = sorted(counts.items(),key=lambda x:x[1],reverse=True)
        ans = ''
        for count in sorted_count:
            ans += count[0]*count[1]
        return ans
