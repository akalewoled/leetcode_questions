from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        t=Counter(t)
        for i in t:
            if i not in s or t[i]>s[i]:
                return i
        