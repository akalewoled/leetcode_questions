
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final=0
        for item in operations:
            final=final + 1 if item[1]=="+" else final - 1
        return final