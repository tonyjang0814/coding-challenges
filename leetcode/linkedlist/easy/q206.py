# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        next_node = None
        while curr is not None:
            curr_node = ListNode(curr.val,None)
            curr_node.next = next_node
            next_node = curr_node
            curr = curr.next
        return next_node