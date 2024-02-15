"""
fiker @a2sv
we intiate two arrays which have the index of senators 
we remove pop an element in fifo order and append the winner index by adding the numbeer of the input array 
beacouse we know the ones who wins  remain in the array and we cant left it where it was beacouse it would remove what is left of it twice
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        r_arr = [i for i in range(len(senate)) if senate[i]=='R']
        d_arr = [j for j in range(len(senate)) if senate[j]=='D']
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
                
        return 'Radiant' if r_arr else 'Dire'
        