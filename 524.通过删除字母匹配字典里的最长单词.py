# 双指针
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = []
        def ifSonString(s:str,t:str) -> bool:
            n1 = 0
            for i in range(len(s)):
                if n1<len(t) and s[i]==t[n1]:
                    n1 += 1
                elif n1>=len(t):
                    return True
            if n1>=len(t):
                return True
            else:
                return False
        for words in dictionary:
            if ifSonString(s,words):
                ans.append(words)
        ans.sort(key=lambda x:(-len(x),x)) #把符合要求的按长度和字母顺序排序
        return ans[0] if ans!=[] else ''
