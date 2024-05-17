# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        if not root1 and not root2:
            return None
        newnode=TreeNode(root1.val+root2.val)
        newnode.left=self.mergeTrees(root1.left,root2.left)
        newnode.right=self.mergeTrees(root1.right,root2.right)
        return newnode
        