# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#   Method 1.
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.order = list()
        self.inorder(root)
        
        return self.order[k-1]
    
    
    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.order.append(root.val)
        self.inorder(root.right)
