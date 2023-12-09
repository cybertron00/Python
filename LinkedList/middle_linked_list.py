# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
In this we have a fast and slow pointer
the fast pointer traverses twice the distance as
slow pointer, so when the fast pointer is at the end 
the slow pointer will be exactly at the middle
'''
class Solution:
    def middleNode(self, head):
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head