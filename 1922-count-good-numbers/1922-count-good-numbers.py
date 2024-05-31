class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # the solution is
        # 5 ** number of even indexes * 4 * number of odd indexes
        # but ir causes TLA for 
        #(5 ** evens * 4 ** odds ) % mod 
        #lets optimaze the power operation using pow(x,n) question

        mod=1000000007 
        
        evens=n//2 + n%2

        odds= n //2
        def power(x,n):# from leet code 50 probelm
            if n==0:
                return 1
            res=power(x,n//2)
            res=res*res
            res=res%1000000007
            return res*x if n%2 else res
        
        return  (power(5,evens)% mod * power(4,odds) %mod ) % mod 

            