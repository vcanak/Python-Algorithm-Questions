"""
ou are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     
     def __str__(self) -> str:
         return f"{self.val}"
     
def add_two(l1,l2):
    added = 0
    root = curr = ListNode(0)
    while l1 or l2 or added:
        if l1: 
            added += l1.val
            l1 = l1.next
        if l2: 
            added += l2.val 
            l2 = l2.next
        curr.next = curr = ListNode(added % 10)
        added //= 10
    
    return root.next

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next =ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next =ListNode(4)

print(add_two(l1,l2))