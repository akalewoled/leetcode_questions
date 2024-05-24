class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysperweight( weightlist:list[int],capacity:int):
            day=0
            car=0
            for i in weightlist:
                if car+i <=capacity:
                    car+=i
                else:
                    day+=1
                    car=0
                    car+=i
            return day+1
        mincapacity=max(weights)
        maxcapacity=sum(weights)
        while mincapacity<=maxcapacity:
            mid=(mincapacity+maxcapacity)//2
            if daysperweight(weights,mid)<=days:
                maxcapacity=mid-1
            elif daysperweight(weights,mid)>days:
                mincapacity=mid+1
        return mincapacity

            