class Solution:
    def sumOfThree(self, n: int) -> List[int]:
        """
        to have the consqutive numbers the number has to be a multiple of theree
        i.e =>i+(i+1)+i+2== num 
            = 3*i+3=num
            =3*i+3(1)=num
            =3(i+1)= num i.e num has to be a  multiple of theree
            i=num//3-1
            """ 
        if n%3==0:
            k=n//3
            return [k-1,k,k+1]
        else:
            return []  
        