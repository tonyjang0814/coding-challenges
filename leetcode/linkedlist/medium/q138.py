"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        
        curr = head
        while curr is not None:
            next_node = curr.next
            new_node = Node(curr.val,next_node,None)
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
            
        curr = head
        while curr is not None:
            print(curr.val)
            next_node = curr.next.next
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = next_node
        
        curr = head
        ans = curr.next
        while curr.next is not None:
            next_node = curr.next
            curr.next = curr.next.next
            curr = next_node
        return ans