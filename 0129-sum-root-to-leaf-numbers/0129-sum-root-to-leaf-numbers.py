# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.final=0

        def backTrack(node,number):


            if not node.right and not node.left:

                self.final+=(int(number+str(node.val)))
                return


            if node.left:

                backTrack(node.left,number+str(node.val))
            if node.right:
                backTrack(node.right,number+str(node.val))
        backTrack(root,"0")
        return self.final
            


        