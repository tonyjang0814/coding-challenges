# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
            
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_idx = bisect.bisect(preorder,root_val)
            
        root.left = self.bstFromPreorder(preorder[:root_idx])
        root.right = self.bstFromPreorder(preorder[root_idx:])
        return root

        