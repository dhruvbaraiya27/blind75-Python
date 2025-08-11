# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverseNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None

        while head:
            forw = head.next
            head.next = prev
            prev = head
            head = forw
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid_node = self.getMiddle(head)
        head1 = head
        head2 = self.reverseNode(mid_node.next)
        mid_node.next = None
        while head1 and head2:
            forw1 = head1.next
            forw2 = head2.next
            head1.next = head2
            head2.next = forw1
            head1 = forw1
            head2 = forw2





        
