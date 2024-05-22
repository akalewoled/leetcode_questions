# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checker(node,lo,hi):
            if not node:
                return True
            
            if lo<node.val<hi:
                return checker(node.left,lo,node.val) and checker(node.right,node.val,hi)
            else:
                return False
            
        return checker(root,float("-inf"),float("inf"))