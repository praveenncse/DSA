# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iteration

        '''prev,curr=None,head
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        return prev'''

        # Recursive

        if head is None:
            return None

        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newHead
        