class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        final=0
        tempo=0
        for i in range(len(plants)):
            tempo+=plants[i]
            
            if tempo<=capacity:
                final+=1
            else:
                final+=i+i+1
                tempo=0
                tempo+=plants[i]
        return final
        