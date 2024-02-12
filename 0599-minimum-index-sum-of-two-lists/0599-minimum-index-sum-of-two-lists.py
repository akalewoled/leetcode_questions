class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a=set(list1)
        b=set(list2)
        c=a&b
        mini = []
        minilen=len(list1)+len(list2)
        for i in c:
            index=list1.index(i)+list2.index(i)
            if index<=minilen :
                minilen=index
        for i in c:
             if list1.index(i)+list2.index(i)==minilen:
                 mini.append(i)
        print(list1)
        print(list2)
        print(c)
        
        return list(mini)
        