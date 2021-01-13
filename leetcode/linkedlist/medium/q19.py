# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-100,head)
        second_ptr = dummy
        first_ptr = dummy
        while n+1 > 0:
            first_ptr = first_ptr.next
            n-=1
        while first_ptr != None:
            second_ptr= second_ptr.next
            first_ptr = first_ptr.next
        
        next_node = second_ptr.next.next
        second_ptr.next.next = None
        second_ptr.next = next_node
        return dummy.next