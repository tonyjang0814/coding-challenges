# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        contents = list()
        for i in range(len(lists)):
            curr1 = lists[i]
            while curr1 is not None:
                contents.append(curr1.val)
                curr1 = curr1.next
        contents.sort()
        dummyNode = ListNode(-1,None)
        start = dummyNode
        for i in contents:
            dummyNode.next = ListNode(i,None)
            dummyNode = dummyNode.next
        return start.next