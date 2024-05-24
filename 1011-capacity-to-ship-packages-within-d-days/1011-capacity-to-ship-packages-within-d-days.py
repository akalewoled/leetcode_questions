class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def requireddays(capacity):
            days=0
            i=0
            load=0
            
            while i< len(weights):
                load+=weights[i]
                
                if load== capacity:
                    days+=1
                    load=0
                elif load > capacity:
                    days+=1
                    load=weights[i]
                
                i+=1
            while load> 0:
                load-=capacity
                days+=1
            return days
        
        l=max(weights)
        r=sum(weights)
        
        while l<=r:
            mid = l+(r-l)//2
            day=requireddays(mid)
            if day > days:
                l=mid+1
            else:
                r=mid-1
        return l
                
            