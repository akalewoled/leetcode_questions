class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        return "[.]".join(address.split("."))
    """
    1st split it using . separetor
    2nd join it using [.]
    """