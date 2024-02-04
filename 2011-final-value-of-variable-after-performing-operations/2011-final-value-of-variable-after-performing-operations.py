
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final=0
        for item in operations:
            final=final + 1 if item[1]=="+" else final - 1
        return final
    """
    for every elemnt in  operations i.e "x++","++x","--x","x--" pick the middle charcter 
    add one to the final number if it is + or minus 1 if it is minus
    """