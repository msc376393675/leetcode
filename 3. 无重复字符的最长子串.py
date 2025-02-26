# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = ''
        res = 0
        n = len(s)
        if n==1 :
            return 1
        while right<n:
            if s[right] in s[left:right]:
                res = max(len(ans),res)
                left += ans.index(s[right])+1
                right += 1
                ans = s[left:right]
            else:
                ans += s[right]
                right += 1
        return max(len(ans),res)
