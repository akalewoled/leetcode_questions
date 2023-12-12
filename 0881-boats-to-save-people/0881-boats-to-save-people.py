class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j =0,len(people)-1
        final=0
        while i<=j:
            sum=people[i]+people[j]
            if sum<=limit:
                final+=1
                i+=1
                j-=1
            else:
                final+=1
                j-=1
        return final

        