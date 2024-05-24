# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxdiff=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def checker(node,maxi,mini):
            if not node:
                return
            maxi=max(maxi,node.val)
            mini=min(mini,node.val)
            self.maxdiff=max(self.maxdiff,maxi-mini)
            checker(node.right,maxi,mini)
            checker(node.left,maxi,mini)
            return
        checker(root,root.val,root.val)
        return self.maxdiff
            
        