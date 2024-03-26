class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
         #the main probelm is to itetate from one set of range to another 
         # solution increment if the fisrt is the end of the first  is less than the end of the senond /there is a space in b
        #           increment the seconf id there the end of the second less than the end of the first /there is a space in first 
         final=[]
         i=j=0
         while i<len(fl) and j<len(sl):
            fl_s,fl_e=fl[i]
            sl_s,sl_e=sl[j]
            if  fl_s<=sl_e and sl_s<=fl_e:# if there is  gap between start of first and end of second and start of second to end of first
                final.append([max(fl_s,sl_s),min(sl_e,fl_e)])
            if fl_e<=sl_e:
                i+=1
            else:
                j+=1
         return final