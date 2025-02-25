# 双指针的应用
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        while left<=right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s_part1 = s[left:right] #删除右边的字母
                s_part2 = s[left+1:right+1] #删除左边的字母
                #判断删除后子串是否回文
                if s_part1==s_part1[::-1] or s_part2==s_part2[::-1]: 
                    return True
                else:
                    return False
        return True
