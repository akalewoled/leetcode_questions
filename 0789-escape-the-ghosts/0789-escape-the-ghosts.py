import math 
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def mag(x1,y1):
            x2=target[0]
            y2=target[1]
            
            mag=abs(x1-x2)+abs(y1-y2)
            return mag
        distance= mag(0,0)
        print(distance)
        for item in ghosts:
            print(mag(item[0],item[1]))
            if mag(item[0],item[1])<=distance:
                return False
        return True
            
            
            
            
        
        
        