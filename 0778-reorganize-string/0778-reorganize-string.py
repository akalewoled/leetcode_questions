from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)

        maxi= max(freq.values())
        if len(s) -maxi+1<maxi:
            return ""
        q=[]
        final=[]
        for i in freq:
            heappush(q,(-freq[i],i))
        
        while len(q)>1:
            X=heappop(q)
            Y=heappop(q)
            final.extend([X[1],Y[1]])
            if X[0]<-1:
                heappush(q,(X[0]+1,X[1]))
            if Y[0]<-1:
                heappush(q,(Y[0]+1,Y[1]))
        if q:
            
            final.append(q[0][1])
        return "".join(map(str,final))

