'''
We need to do following:
1. init a prev and curr pointer
2. in the loop 1st re-map the next pointer to prev(swapping)
3. in the loop 2nd shift the present pointers to next state
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None     
        curr = head 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
 