class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        check=[0] * (n+1)
        
        for i in range(n-1,-1,-1):
            include=questions[i][0]+(check[i+ questions[i][1]+1] if i+questions[i][1]+1 <n else 0)
            exclude=check[i+1]
            check[i]=max(include,exclude)
        return check[0]