class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        finalarray=[]
        finalDict={}
        for i in cpdomains:#i="900 google.com"
            k=i #
            array=k.split(" ")# array =["900", "google.com"]
            value=array[0]
            domains=array[1].split(".")# domains =["google" ,"com"]
            for k in range(0,len(domains)):
                string=".".join(domains[k:])
                if string in finalDict:
                    finalDict[string]=int(finalDict[string])+int(value)
                else:
                    finalDict[string]=int(value)
        for j in finalDict:
            befit=finalDict[j]
            bohala=j
            newjoin=[]
            newjoin.append(str(befit))
            newjoin.append(str(bohala))
            newstring=" ".join(newjoin)
            print(newstring)
            finalarray.append(newstring)
        return(finalarray)
