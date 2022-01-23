# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(root):
            #   The base case
            if root is None:
                return [0]
            if root.left is None and root.right is None:
                return [1]
            
            #   The content
            left_node_dist = dfs(root.left)
            right_node_dist = dfs(root.right)
            
            for left_dist in left_node_dist:
                for right_dist in right_node_dist:
                    if left_dist != 0 and right_dist != 0 and left_dist + right_dist <= distance:
                        self.ans += 1
            newNode = []
            for left_dist in left_node_dist:
                if left_dist!= 0 and left_dist + 1 < distance:
                    newNode.append(left_dist + 1)
            
            for right_dist in right_node_dist:
                if right_dist!=0 and right_dist + 1 < distance:
                    newNode.append(right_dist + 1)
            return newNode
        
        dfs(root)
        return self.ans