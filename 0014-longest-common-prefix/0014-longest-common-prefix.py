class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check(i):
            fixed=strs[0]
            for items in strs:
                if i > len(items)-1 or items[i]!= fixed[i]:
                    return False
            return True
        i=0
        while True:
            if check(i):
                i+=1
            else:
                return strs[0][:i]
        