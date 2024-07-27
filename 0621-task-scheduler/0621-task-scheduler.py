from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq= [0]*26
        for task in tasks:
            freq[ord(task)-ord('A')]+=1
        freq.sort(reverse=True)
        max_len=freq[0]-1
        empty = max_len* n

        for i in range(1,26):

            empty-=min(max_len,freq[i])
        
        return empty+len(tasks) if empty > 0 else len(tasks)

         