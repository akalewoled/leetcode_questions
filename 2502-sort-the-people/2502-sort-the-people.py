class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        binding=dict(zip(heights,names))
        heights=sorted(binding,reverse=True)
        final=[binding[height] for height in heights]
        return final