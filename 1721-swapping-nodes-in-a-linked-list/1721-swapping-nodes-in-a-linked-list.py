# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        n  =  head
        for _ in range(k-1):
            n  =  n.next
        
        a  =  n
        b  =  head
        
        while n.next:
            b  =  b.next
            n  =  n.next
        
        a.val, b.val  =  b.val, a.val
        
        return head