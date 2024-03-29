# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            
            val = carry + v1 + v2
            result.next = ListNode(val%10)
            result, carry = result.next, val//10
            
        if carry:
            result.next = ListNode(carry)
            
        return dummy.next
'''
Pseudocode:
Take the last index of each array
Add them together
Reverse the sum
Return the reversed sum
'''
