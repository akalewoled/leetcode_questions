# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # change the  tree to list and divide the lsit 
        
        array=[]
        def bfs(node): 
            if not node :
                return 
            bfs(node.left)
            array.append(node.val)
            bfs(node.right)
        bfs(root)
        #breaking it to balanced binrary ttree
        def breaker(arr):
            if not arr:
                return
            mid = len(arr) // 2
			
            root = TreeNode()
            root.val=arr[mid]
            
            root.left = breaker(arr[:mid])
            
            root.right = breaker(arr[mid + 1:])
            
            return root
        
        return(breaker(array))
        
        
            