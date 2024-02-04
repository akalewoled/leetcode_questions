from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        t=Counter(t)
        for i in t:
            if i not in s or t[i]>s[i]:
                return i
        """
        1st we import Counter from collection  to count the reputition
        2nd iterate through the counter to get the diffrentce
        3rd if a number is not in the first word or its occurance is greter in the second number return it
        """