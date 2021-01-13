# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #   Count total number of nodes in linked list and if less than 2, just return its head
        count = 0
        curr = head
        while curr != None:
            count+=1
            curr=curr.next
        if count < 2:
            return head
        
        curr = head
        second_head = curr.next
        prev = None
        while curr.next!= None:
            prev = curr
            next_temp = curr.next
            curr.next = curr.next.next
            curr = next_temp
        if count %2 == 0: # if even number of linked list
            prev.next = second_head
        else:   #if odd number of linked list
            curr.next = second_head
        return head