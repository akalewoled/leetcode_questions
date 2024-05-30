# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can convert the tree to a array  recursivly and return the kth element
        # letsroot try to implent inorder traversal using stack 
        curr=root.left
        stack=[root]
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            
            tempo=stack.pop()
            k-=1
            if k==0:
                return tempo.val
            curr=tempo.right