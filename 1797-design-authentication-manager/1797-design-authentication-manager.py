class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens={}
        self.timeToLive=timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=currentTime+self.timeToLive
        

        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId]>currentTime :
            self.tokens[tokenId]=self.timeToLive+currentTime

        

    def countUnexpiredTokens(self, currentTime: int) -> int:
   
        keys=[]
        for i in self.tokens:
            if self.tokens[i]-currentTime<=0:
                keys.append(i)

# Delete items from the dictionary using the stored keys
        for key in keys:
            del self.tokens[key]
        
        return len(self.tokens)



       
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)