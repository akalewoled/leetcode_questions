"""
fikiremariyam @a2sv
the question is asking to fined the face of a card  the smallet number where is is not repated in its back side
 so we start by filtring the repated front abd back 
 then we merje the two arrays and fined the minimum  which is not in 
 """
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same_numbers = set(fronts[i] for i in range(len(fronts)) if fronts[i]==backs[i])
        cards=sorted( fronts+backs)
        for i in range(len(cards)):
            if cards[i] not in same_numbers:
                return cards[i]
        return 0