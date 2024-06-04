class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.possible_combo=[]
        def genrate_comb(curNum,cur_list):
            if len(cur_list) == k:
                self.possible_combo.append(cur_list)
                return
            for num in range(curNum +1 , n+ 1):
                genrate_comb(num,cur_list + [num])
        for curNum in range(1, n+1):
            genrate_comb(curNum,[curNum])
        return self.possible_combo
                    
        