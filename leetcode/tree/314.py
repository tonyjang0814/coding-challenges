# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = dict()
        que = deque([(root,0)])
        while que:
            root,state = que.popleft()
            if root is None:
                continue
            if state not in table:
                table[state]=[root.val]
            else:
                table[state].append(root.val)
            que.append((root.left,state-1))
            que.append((root.right,state+1))
        ans = list()
        for key in sorted(table.keys()):
            ans.append(table[key])
        return ans