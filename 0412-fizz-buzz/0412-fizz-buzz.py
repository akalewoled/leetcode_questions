class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final=[]
        for i in range(1,n+1):
            if i%15==0:
                final.append("FizzBuzz")
                continue
            elif  i%5==0:
                final.append("Buzz")
            elif i%3==0:
                final.append("Fizz")
            else:
                final.append(str(i))
        return final
        