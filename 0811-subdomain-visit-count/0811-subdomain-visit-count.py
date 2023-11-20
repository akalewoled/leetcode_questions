class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        final=[]# the final value that is about to be returned
        linksamount={}
        def recursivve(amount,listoflinks):#recursive function that scounte the reptition of each domain and sub domain
            
            if len(listoflinks)==1:# base case in case of "com" is left
                linksamount[listoflinks[0]]=amount+linksamount.get(listoflinks[0] ,0)
                return
            link=".".join(listoflinks)
            linksamount[link]=amount+linksamount.get(link,0)
            recursivve(amount,listoflinks[1:])
            
        #for every  links and number of request 
        for  items in cpdomains:
            
            times,link=items.split()#times is the number of request and link is the actual link
        
            recursivve(int(times),list(link.split(".")))
        print(linksamount,end="end\n")
        
        #we print the domains and the amount of request 
        for  link,request in linksamount.items():
            agrigate=[]
            
            agrigate.append(str(request))
            agrigate.append(link)
            print(agrigate)
            agrigate=" ".join(agrigate)
            final.append(agrigate)
        
        return final