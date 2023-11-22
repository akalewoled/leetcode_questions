class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        array1=[0]*(len(s)+1)#we add one beacouse we add or substract if  the final number is the last index
        for begin,end,val in shifts:
            if val==1:
                array1[begin]+=1#[0,+1,0,0,0] for shisfts (1,2,1)
                array1[end+1]-=1#[0,+1,0,-1,0] decrement at n+1 so that the number loose its iffect on the calculation on the prefix sum later
            else:
                array1[begin]-=1
                array1[end+1]+=1
        #calculate the prefix sum
        prefix_sum = [0] * len(array1)

        # Calculate prefix sum
        prefix_sum[0] = array1[0]
        for i in range(1, len(array1)):
            prefix_sum[i] = prefix_sum[i-1] + array1[i]
        # Print prefix sum
        print(prefix_sum)
        final=[]#string to br recorderd
        for i in range(len(s)):
            asci=ord(s[i])
            asci=asci-97
            asci=asci+prefix_sum[i]
            asci=asci%26
            asci=asci+97
            final.append(chr(asci))
        return "".join(final)
        # adjust the string

            