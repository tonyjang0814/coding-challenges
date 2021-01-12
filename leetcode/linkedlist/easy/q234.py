# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None:
            return True
        elif head.next is None:
            return True
        #   Count length of linked list
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        
        #   iterate through linked list unil half
        half = count // 2
        curr = head
        while half> 0:
            curr = curr.next
            half -= 1
            
        #   reverse link list from then
        prev = None
        _next = None
        while curr is not None:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        
        
        #   iterate both linked list (head and another reversed head) and compare if palindrome.
        left,right = 0, count
        curr = head
        while left < right:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
            left += 1
            right -= 1
        return True