class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divcon(s):
		     
            if len(s) < 2:
                return ""
            
            pivot = []
            for i, ch in enumerate(s):
                if ch.isupper() and ch.lower() not in s:
                    pivot.append(i)
                if ch.islower() and ch.upper() not in s:
                    pivot.append(i)
            if not pivot:
                return s
            else:
                mid = (len(pivot)) // 2
                return max(divcon(s[:pivot[mid]]),divcon(s[pivot[mid]+1:]),key=len)
        
        return divcon(s)