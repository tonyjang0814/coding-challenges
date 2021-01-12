# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(-100,None)
        dummy = ans
        curr1,curr2 = l1,l2
        factor = 0
        while curr1 and curr2:
            _sum = (curr1.val + curr2.val) + factor
            # curr1.val = _sum % 10
            ans.next = ListNode(_sum % 10,None)
            if _sum >= 10:
                factor = _sum // 10
            else:
                factor = 0
            curr1 = curr1.next
            curr2 = curr2.next
            ans = ans.next
        
        while curr1:
            _sum = (curr1.val + factor)
            # curr1.val = _sum % 10
            ans.next = ListNode(_sum % 10,None)
            if _sum >= 10:
                factor = _sum // 10
            else:
                factor = 0
            curr1 = curr1.next
            ans = ans.next
            
        while curr2:
            _sum = (curr2.val + factor)
            # curr1.val = _sum % 10
            ans.next = ListNode(_sum % 10,None)
            if _sum >= 10:
                factor = _sum // 10
            else:
                factor = 0
            curr2 = curr2.next
            ans = ans.next
        
        if factor > 0:
            ans.next = ListNode(factor,None)    
        
        return dummy.next